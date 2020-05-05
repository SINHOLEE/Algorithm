# Javascript 기본 도구

### 문자 정렬 sort

```javascript
// 오름차순

const arr = ['a', 'b', 'f', 'd', 'c', 'a']

arr.sort()

console.log(arr) // [ 'a', 'a', 'b', 'c', 'd', 'f' ]

// 내림차순

const arr = ['a', 'b', 'f', 'd', 'c', 'a']

arr.sort(function(a, b){
    return b.charCodeAt() - a.charCodeAt();
})

console.log(arr) // [ 'f', 'd', 'c', 'b', 'a', 'a' ]


```

### 2차배열 생성

```javascript
const n = 3;
const m = 5;

let arr = Array.from(Array(n), ()=>Array(m));
let c = 1;

for (let i = 0; i < 3; i++){
    for (let j = 0; j < 5; j++){
        arr[i][j] = c;
        c++;
    }
    console.log(arr[i])
}
/*
[ 1, 2, 3, 4, 5 ]
[ 6, 7, 8, 9, 10 ]
[ 11, 12, 13, 14, 15 ]
*/
```



### arr to string

```javascript
var arr = ["a", "b", "c", "d", "e"];
var arr_join = arr.join();
console.log(arr_join);
// a,b,c,d,e


var arr1 = ["a", "b", "c", "d", "e"];
var arr_join1 = arr1.join("/");	
console.log(arr_join1);
// a/b/c/d/e
```



### string to Lowercase

```javascript
let str1 = 'ADVwsW'
str1 = str1.toLowerCase();
console.log(str1); //abvwsw
```



### string to ascii code

```javascript
'a'.charCodeAt();
// 97
```



### ascii to string

```javascript
String.fromCharCode(97);
// a
```



### arr for reduce

```javascript
// 원본 배열
var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

var result = arr.reduce(function(previousItem, currentItem, index, array) {
// 반환된 결과는 다음번 콜백의 첫번째 파라미터로 다시 전달된다.
	return previousItem + currentItem;
}, 0);

// 메소드 수행 후 원본 배열
console.log(arr);
// 메소드 수행 후 리턴값은 0부터 10까지의 합
```



### Object forloop

```javascript
const obj = {'a': 1, 'b':2, 'c':3};
for (const[key, value] of Object.entries(obj)) {
    console.log(key, value);
};
/*
a 1
b 2
c 3
*/

// object의 value만 뽑아서 루프 돌리기
const aa = Object
.values(obj)
.reduce((prev, curr)=>{
    return prev + curr;
},0);
// 6

```



### arr methods

```javascript
let arr = [1, 2, 3, 4];

const a = arr.pop(); // 4, arr = [1, 2, 3]

const b = arr.shift(); // 1 , arr = [2, 3]

arr.push(2); // append
```

