class Rectangle {
    constructor(w, h) {
        this.w = w;
        this.h = h;
    }
}
    
/*
 *  Write code that adds an 'area' method to the Rectangle class' prototype
 */
// funtion으로 정의하면 this가 해당 object에 바인딩 된다.
// Rectangle.prototype.area = function() {
//     return this.w * this.h;
// };

// prototype을 알아야 이해할 수 있을 듯 하다.
// 화살표 함수 쓸 때는 this가 Reactange Object에 바인딩 되지 않는다.
Rectangle.prototype.area = ()=> {
    console.log(this);
    return this.w * this.h;
};

// 화살표 함수로 정의한 함수는 상위 컨텍스트가 전역 컨텍스트이므로 window를 나타내고 function으로 정의한 함수는 자신을 정의한 객체를 나타낸다.
// this가 없을 때는 new를 통해 객체 생성이 불가능하다.
/*
 * Create a Square class that inherits from Rectangle and implement its class constructor
 */
class Square extends Rectangle{
    constructor(side){
        super(side, side);
    }
    
}


if (JSON.stringify(Object.getOwnPropertyNames(Square.prototype)) === JSON.stringify([ 'constructor' ])) {
    const rec = new Rectangle(3, 4);
    const sqr = new Square(3);
    
    console.log(rec.area());
    console.log(sqr.area());
} else {
    console.log(-1);
    console.log(-1);
}