// // 모범답안.

// class Polygon {
//     constructor(sides) {
//         console.log(this);
//         this.sides = sides;
//     }
    
//     perimeter() {
//         return this.sides.reduce( (a, b) => a + b );
//     }
// }

// // 내답

// class Polygon{
//     constructor(arr){
//         this.lengths = arr;
//     }

//     perimeter(){
//         return this.lengths.reduce((prev, curr)=>{
//             return prev + curr;
//         },0);
//     }
// }

// 내식대로 이해하기

const person= {

    name: "sinho",
    age: 29,
    getAge(){
        return this.age;
    },
    addOneAge(){
        this.age++;
    }
}

console.log(person.age);
console.log(person.getAge());
const getSinhoAge = person.getAge.bind(person); // 이걸 어떻게 해결하지?
console.log(getSinhoAge());