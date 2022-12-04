let friends=["name1","name2","name3"]
let list=""
friends.forEach((s)=>{
    console.log(s)
    list += `  <a href="/user.html"><li><button class="friend">${s}</button></li></a>`;



document.getElementById('friendlist').innerHTML =list;
