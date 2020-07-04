// this에 대한 오해
// 1 자기 자신을 가리킨다.
// 2 해당 스코프를 가리킨다.

console.log(this); // {} -> 전역변수를 뜻하고, 브라우저에서는 window를 뜻한다.

function fn(){
    b= 1;
}

fn();

console.log(b); 
console.log(this);
// 내 예상 ->1 왜? b는 전역변수로 작용하니까.

// function fn1(){
//     var b = 2;
// }

// fn1();
// console.log(b)
// 내예상 b를 전역으로 선언한 fn()이 있다면 1 없다면 선언 오류


var obj = {
    a: 10,
    fnc(){
        console.log(this.a);
    }
}

// obj.fnc(); // 10
var temp = obj.fnc;
temp(); // undefined 왜??? this는 현재 전역을 가리키고 있고, 전역에 a라는 변수가 할당되어 있지 않기 때문에
// this는 실행시점에 생성된다 그리고 그 실행하는 함수에서, 닷(.)으로 마지막으로 바인딩 된 객체를 가리키고, 만약 없으면 전역(window)를 가리킨다.
// 이게 무슨 의미지?
// 여기서 this.a를 바꾸고 싶은데, temp()를 통해서 바꾸고 싶다면 bind(obj)를 이용해서 바꿔야한다.
// ex

var obj2 = {
    a: 12,
    setA(){
        this.a = 555;
    }
}

// obj2.setA(123);
console.log(obj2.a);

var  tempFunc = obj2.setA;
setTimeout(obj2.setA, 1000); // 12
setTimeout(obj2.setA.bind(obj2), 1000); // 555
// 왜? 첫번째 타임아웃 함수에서 실행되는 함수는 var temp = obj2.setA; temp()와 같은의미로  this를 전역으로 가리킨다.
// 그래서 this를 명시적으로 바인딩 하기 위해서는 .bind(obj2)라는 용법을 이용하던가, call, apply를 이용한다.
setTimeout(() => {
   console.log(obj2.a); 
}, 1100);

