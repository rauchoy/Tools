chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "checkURL") {
      const urlToCheck = request.url;
      const apiKey = "7ea29bc36d28907e72023d19302cb1bcff81f352fa6dce3b802ab91f6f743f99"; // Remove actual API key before push
      const apiUrl = `https://www.virustotal.com/api/v3/urls`;
  
      fetch(apiUrl, {
        method: 'POST',
        headers: {
          'x-apikey': apiKey,
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
          url: urlToCheck
        })
      })
     .then(response => response.json())
     .then(data => {
        let resultText = "";
        if (data.data && data.data.id) {
          const analysisUrl = `https://www.virustotal.com/gui/url/${data.data.id}/detection`;
          resultText = `URL submitted. View analysis here: ${analysisUrl}`;
        } else if (data.error) {
          resultText = `Error: ${data.error.message}`;
        } else {
          resultText = "Could not retrieve analysis information.";
        }
        chrome.runtime.sendMessage({ action: "displayResult", result: resultText });
      })
     .catch(error => {
        chrome.runtime.sendMessage({ action: "displayResult", result: `Error: ${error.message}` });
      });
    }
  });