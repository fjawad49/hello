import scipy.stats as st
import numpy as np


def adjust_threshold(threshold, symbol):
    """
    Adjusts the threshold based on the provided comparison symbol.

    Arguments:
    threshold (float): The value to be adjusted.
    symbol (str): The comparison symbol. Options are '>', '>=', '<', '<='.

    Returns:
    float: Adjusted threshold value.
    """
    if symbol == ">":
        return threshold + 0.5
    elif symbol == ">=":
        return threshold - 0.5
    elif symbol == "<":
        return threshold - 0.5
    elif symbol == "<=":
        return threshold + 0.5
    else:
        raise ValueError(
            f"Invalid symbol: {symbol}. Use '>', '>=', '<' or '<='."
        )


def calculate_z_score(x, mu, std):
    """
    Computes the z-score.

    Arguments:
    x (float): The data point.
    mu (float): The population mean of the distribution.
    std (float): The standard deviation of the distribution.

    Returns:
    float: The z-score.
    """
    return (x - mu) / std


def normal_approximation_to_binomial(threshold, n, p, symbol):
    """
    Applies a normal approximation to a binomial distribution and
    returns the probability.

    Arguments:
    threshold (float): The threshold value for the binomial distribution.
    n (int): The number of trials.
    p (float): The probability of success in each trial.
    symbol (str): The comparison symbol. Options are '=', '>', '>=', '<', '<='.

    Returns:
    float: The probability based on the normal approximation.
    """
    mu = n * float(p)
    std = np.sqrt(n * p * (1 - p))

    if symbol == "=":
        return (st.norm.cdf(calculate_z_score(threshold + 0.5, mu, std)) -
                st.norm.cdf(calculate_z_score(threshold - 0.5, mu, std)))

    adjusted_threshold = adjust_threshold(threshold, symbol)
    z_score = calculate_z_score(adjusted_threshold, mu, std)

    if symbol in [">", ">="]:
        return 1 - st.norm.cdf(z_score)
    elif symbol in ["<", "<="]:
        return st.norm.cdf(z_score)


# Example output usage
print(normal_approximation_to_binomial(150, 300, 0.53, ">="))
