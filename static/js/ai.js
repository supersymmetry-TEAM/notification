
      // More API functions here:
      // https://github.com/googlecreativelab/teachablemachine-community/tree/master/libraries/image
  
      // the link to your model provided by Teachable Machine export panel
      const URL = "https://teachablemachine.withgoogle.com/models/qQ3EwBtIl/";
  
      let model, webcam, labelContainer, maxPredictions;
  
      // Load the image model and setup the webcam
      async function init() {
          const modelURL = URL + "model.json";
          const metadataURL = URL + "metadata.json";
  
          // load the model and metadata
          // Refer to tmImage.loadFromFiles() in the API to support files from a file picker
          // or files from your local hard drive
          // Note: the pose library adds "tmImage" object to your window (window.tmImage)
          model = await tmImage.load(modelURL, metadataURL);
          maxPredictions = model.getTotalClasses();
  
  
          // append elements to the DOM
          labelContainer = document.getElementById("label-container");
          for (let i = 0; i < maxPredictions; i++) { // and class labels
              labelContainer.appendChild(document.createElement("div"));
          }
      }
  
  
      // run the webcam image through the image model
      async function predict() {
          // predict can take in an image, video or canvas html element
          var image1 = document.getElementById("girl_body")
          const prediction = await model.predict(image1,false);
          prediction.sort((a,b)=>parseFloat(b.probability)-parseFloat(a.probability))
          console.log(prediction[0].className)
          var resultmessege;
          switch(prediction[0].className){
              case "a":
                  resultmessege="she is A cup"
                  break;
              case "b":
                resultmessege="she is B cup"
                  break;
              case "c":
                resultmessege="she is C cup"
                  break;
              case "d":
                resultmessege="she is D cup"
                  break; 
          }
          $('.result-messege').html(resultmessege);
      
          document.getElementById('label-container0').style ="width:"+ prediction[0].probability.toFixed(2)*100+"%";
          document.getElementById('label-container0').innerHTML =prediction[0].className + ": "+prediction[0].probability.toFixed(2)*100+"%";
          
          document.getElementById('label-container1').style ="width:"+ prediction[1].probability.toFixed(2)*100+"%";
          document.getElementById('label-container1').innerHTML =prediction[1].className + ": "+prediction[1].probability.toFixed(2)*100+"%";
          
          document.getElementById('label-container2').style ="width:"+ prediction[2].probability.toFixed(2)*100+"%";
          document.getElementById('label-container2').innerHTML =prediction[2].className + ": "+prediction[2].probability.toFixed(2)*100+"%";
          
          document.getElementById('label-container3').style ="width:"+ prediction[3].probability.toFixed(2)*100+"%";
          document.getElementById('label-container3').innerHTML =prediction[3].className + ": "+prediction[3].probability.toFixed(2)*100+"%";
      }
