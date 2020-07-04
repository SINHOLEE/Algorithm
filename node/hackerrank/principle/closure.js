// function init(){
//     const name = "sinho";
//     function displayName(){
//         // const name = "in_display_name";
//         console.log("그냥 name ", name); // in_display_name
//         // console.log(this.name); // undefined
//         // console.log("this.name ", this.name);
//         // console.log(scope);
//         // console.log(scope.name);
//         var a = 1;
//     }
//     // if(name !== "aa"){
//     //     var a = 1;
//     // }
//     displayName();
//     console.log(a);
// }

// init();


let a = "1";
function outer () {
	let b = "2"
	return () => {
        let c = "3";
        console.log(a);
        console.log(b);
        console.log(c);
        console.log(a, b, c);
    }
    
};

let inner = outer();
inner();
inner();

// inner = () => console.log("no closure")


// 이때, outer함수를 실행하면서 outer 실행 컨택스트가 실행, lexical scope는 a, 와 b, anonymous를 호출할 수 있음
// return을 anonymous 함수를 호출하기 때문에, 이 함수를 실행은 하지 않는다.
// 33번째 줄에서 console.log(inner()); 하면서 anonymous 실행,  컨택스트 실행
// 이때 anonymous의 lexical scpoe는 a, b, c 모두 접근 가능한 스코프이다.
// 왜? lexical scope는 parser가 code를 읽을때 정하기 때문
// 반환을 


