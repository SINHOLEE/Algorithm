// var 호이스팅 : 변수의 선언과 할당을 구분하겠다는 개념(var에서만)
// 콜백 큐
// 이벤트 루프
// 클로저

for(var i=0; i<5; i++){
    (function(el){
        setTimeout(function() {
            console.log(el);
        }, 1000);
    }(i));
}

// function findUser(id, callback){
//     setTimeout(() => {
//         callback({id:id, name: "사용자 # " +  id})
//     }, 1000);
// }

// function findUsers(ids){
//     // var i;
//     // for (i in ids){ 이렇게 호이스팅 되므로, 1초 뒤에 출력되는 ids[i]는 마지막 19를 가리키게 된다.
//     for(var i in ids){
//         findUser(ids[i], function(user){
//             console.log("사용자 id", ids[i]);
//             console.log("사용자 정보", user);
//         })
//     }
// }

// findUsers([1,23,44,12,19]);
// 출처: https://www.daleseo.com/js-var-issues/

// function callYOU(){
//     var myname = "james";
//     callAdam();
// }

// function callAdam(){
//     return myname;
// }
// callYOU(); // error


// 우리가 기대할때는 callAdam을 호출하는 시점에 분명 myname변수가 함수내에 선언이 되어있고 
// 그 다음에 호출하는 callAdam이 myname 변수에 접근을 할수 있을 것이라고 기대를 합니다.
// 그러나 에러가 발생합니다. 
// 이유는 변수는 함수가 호출하는 시점이 아닌 함수가 정의 되는 시점에 생성이 되기 때문입니다. 
// callAdam이 정의 되는 시점에 myname이라는 변수는 callYOU 함수 안에서만 존재합니다. 당연히 지역변수입니다. 
// 즉, 외부 함수에서는 접근이 안된다는 말입니다.
// 최종보스 글
// 출처: https://yubylab.tistory.com/entry/자바스크립트-변수로-자바스크립트-이해하기 [Yuby's Lab.]



// 실행컨택스트 **핵심**
// 자바스크립트의 code 3가지 분류: global code, function code, eval code(이게 뭐야)
// 이 모든 종류의 code는 실행 컨택스트에 들어와 실행된다(컨테이너같은 개념인가?)
// 클로벌 컨택스트의 경우, 오직 하나만 존재하는 반면, func 컨택스트, eval 컨택스트는 하나의 프로그램에 여러개가 존재가능

//ex
function foo(bar){}
foo(10)
foo(20)
foo(30)

// 위와 같이 동일한 함수를 다른 인자를 받아서 실행할 경우, 이미 존재하는 컨택스트를 사용하는 게 아니라, 
// 새로운 컨택스트를 생성하여 실행한다.

var x = 1;

function foo2() {
  var x = 10;
  bar2();
}

function bar2() {
  console.log(x);
}

foo2(); // ?
bar2(); // ?