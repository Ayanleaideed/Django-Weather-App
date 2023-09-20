function toggleSubmit() {
            const cityInput = document.getElementById('cityInput');
            const submitButton = document.getElementById('btn-submit');

            if (cityInput.value.trim() !== '') {
              submitButton.disabled = false;
              submitButton.style.backgroundColor = "Blue";
            } else {
              submitButton.disabled = true;
              submitButton.style.backgroundColor = "Red";
            }
          }

          // Call toggleSubmit initially to set the initial state of the button
          toggleSubmit();
