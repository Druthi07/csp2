// Add your own functionality here
const generateButton = document.getElementById('generateButton');
const userPrompt = document.getElementById('userPrompt');

// generateButton.addEventListener('click', () => {
//     const prompt = userPrompt.value;
//     // Implement AI image generation logic here
//     // Display generated images and download buttons
// });


const prompt1=document.getElementById('prompt1');
const prompt2=document.getElementById('prompt2');
const prompt3=document.getElementById('prompt3');
const query_imput=document.getElementById('query');

prompt1.addEventListener('click', () => {
    query_imput.value="Textile Embrodiery"
});
prompt2.addEventListener('click', () => {
    query_imput.value="Textile Patterns"
});
prompt3.addEventListener('click', () => {
    query_imput.value="Textile Motifs"
});

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
  }
  
  /* Set the width of the side navigation to 0 */
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }