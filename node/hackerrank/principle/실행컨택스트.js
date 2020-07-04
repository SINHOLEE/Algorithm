console.log(123123123);
test1_1();

function test1_1(){
    let a = 2;
    const arr = [1,2,3];
    b = 123;
    console.log(1);
    console.log(a);
    console.log(arr);

}
var test1_2 = 2;

var test1_3 = function(){
    console.log(2);
}

//그림을 그리면, 
// 1 parser가 모든 변수와 함수 선언을 실행 컨택스트 안에 변수 테이블에 공간을 둔다.
// 2 코드 순서대로 실행한다.