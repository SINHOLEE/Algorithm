// 원본 배열
var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

var result = arr.reduce(function(previousItem, currentItem, index, array) {
    // 반환된 결과는 다음번 콜백의 첫번째 파라미터로 다시 전달된다.
    console.log(index, array);
    //
    array[index] += previousItem; 

	return previousItem + currentItem;
}, 0);

// 메소드 수행 후 원본 배열
console.log(arr);
console.log(result);
// 메소드 수행 후 리턴값은 0부터 10까지의 합