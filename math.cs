using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

IWebDriver driver = new FirefoxDriver(); // Replace with your preferred driver

// Locate the login button using CSS selector
IWebElement loginButton = driver.FindElement(By.CssSelector("button#loginBtn"));

// Click the button
loginButton.Click();


