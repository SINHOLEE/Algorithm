// function hello(x){
//     console.log(x + " asdasdasd");
// }

// hello["woman"] = "what ?"
// hello("sinho");
// console.log(hello.woman);

// var dog = {
//     name: "bekgo",
//     bark: function() { console.log("멍멍")},
//     callDog: function(){console.log(this.name + " 이리와!")},
//     callDog2: ()=>{console.log(this.name+" 이리온")}
// }

// dog.callDog2();


var speech = "this is global value";

var williamShakespeare = {
    speech: "williamShakespeare said ~~~~~",
    sayIt: displayQuote
}

function displayQuote(){
    console.log(this.speech + "!!!!!");
}

williamShakespeare.sayIt();
displayQuote();