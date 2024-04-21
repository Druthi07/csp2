
const generateButton = document.getElementById('generateButton');
const userPrompt = document.getElementById('userPrompt');

const prompt1 = document.getElementById('prompt1');
const prompt2 = document.getElementById('prompt2');
const prompt3 = document.getElementById('prompt3');
const query_imput = document.getElementById('query');

prompt1.addEventListener('click', () => {
    query_imput.value = "Textile Embrodiery"
});
prompt2.addEventListener('click', () => {
    query_imput.value = "Textile Patterns"
});
prompt3.addEventListener('click', () => {
    query_imput.value = "Textile Motifs"
});

document.getElementById('modify').addEventListener('click', () => {
    const imag_path = prompt("Enter Image path");
    axios.post(`http://127.0.0.1:10000/modify`, { path: imag_path, prompt_inp: query_imput.value }, {
        mode: 'no-cors', headers: {
            'Access-Control-Allow-Origin': '*',
        }
    }).then(res => {
        console.log(res.data); document.getElementById('pixres').src = res.data[0]; document.getElementById('pixresedit').src = res.data[1]; })
})
document.getElementById('new').addEventListener('click', () => {
    axios.post(`http://127.0.0.1:10000/new`, { prompt_inp: query_imput.value }, {
        mode: 'no-cors', headers: {
            'Access-Control-Allow-Origin': '*',
        }
    }).then(res => {
        console.log(res.data); document.getElementById('pixres').src = res.data})
})

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}


const onsubTextToImage = (event, id1, id2) => {
    event.preventDefault()
    var output = ''
    console.log(text)
    axios(`http://127.0.0.1:8000/login?text=${text}`, {
        method: "GET", mode: 'no-cors', headers: {
            'Access-Control-Allow-Origin': '*',
        }
    }).then(res => { document.getElementById('result').innerHTML = res.data })
}