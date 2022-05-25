// preload.js

const { read } = require('fs');

// All of the Node.js APIs are available in the preload process.
// It has the same sandbox as a Chrome extension.

callPython = (imagePath) => {
  let dataToSend = ''
  const {spawn} = require('child_process');
  const python = spawn('python-env/Scripts/python.exe', ['test.py', imagePath]);

  python.stdout.on('data', function(data) {
    dataToSend = data.toString();
  })

  python.on('close', (code) => {
    const imagePath = document.getElementById("image-path")
    if(imagePath) imagePath.innerHTML = dataToSend

    // Show processed image
    fetch(dataToSend).then((response) => {
      return response.blob()
    }).then((blob) => {
      console.log(blob)
      const reader = new FileReader()
      reader.readAsDataURL(blob)
      reader.addEventListener("load", () => {
        document.querySelector("#processed-image").style.backgroundImage = `url(${reader.result})`
      })
    })
  })

}

window.addEventListener('DOMContentLoaded', () => {
  const replaceText = (selector, text) => {
    const element = document.getElementById(selector)
    if (element) element.innerText = text
  }


  for (const dependency of ['chrome', 'node', 'electron']) {
    replaceText(`${dependency}-version`, process.versions[dependency])
  }

  const processButton = document.getElementById('process-button')
  if (processButton) {
    processButton.addEventListener('click', () => { 
      const imageInput = document.querySelector("#image_input")
      if (imageInput.files.length > 0) {
        callPython(imageInput.files[0].path)
      } else {
        callPython('undefined')
      }
    })
  }
})

