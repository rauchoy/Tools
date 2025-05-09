document.addEventListener('DOMContentLoaded', function() {
    const checkButton = document.getElementById('checkButton');
    const urlInput = document.getElementById('urlInput');
    const resultDiv = document.getElementById('result');
  
    checkButton.addEventListener('click', function() {
      const urlToCheck = urlInput.value;
      if (urlToCheck) {
        chrome.runtime.sendMessage({ action: "checkURL", url: urlToCheck });
        resultDiv.textContent = "Checking...";
      } else {
        resultDiv.textContent = "Please enter a URL.";
      }
    });
  
    chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
      if (request.action === "displayResult") {
        resultDiv.textContent = request.result;
      }
    });
  });