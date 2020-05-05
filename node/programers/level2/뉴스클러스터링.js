function solution(str1, str2) {
    var answer = 0;
    const number = 65536;
    str1 = str1.toLowerCase();
    str2 = str2.toLowerCase();
    let a_obj = {};
    let b_obj = {};
    for(let i = 0; i<str1.length-1; i++){
        if( 97 <= str1[i].charCodeAt() && str1[i].charCodeAt() <= 122 && 97 <= str1[i+1].charCodeAt() && str1[i+1].charCodeAt() <= 122){
            if (a_obj[str1[i]+str1[i+1]] === undefined){
                a_obj[str1[i]+str1[i+1]] = 1;
            } else {
                a_obj[str1[i]+str1[i+1]] += 1;
            };
        };
    };
    for(let i = 0; i<str2.length-1; i++){
        if( 97 <= str2[i].charCodeAt() && str2[i].charCodeAt() <= 122 && 97 <= str2[i+1].charCodeAt() && str2[i+1].charCodeAt() <= 122){
            if (b_obj[str2[i]+str2[i+1]] === undefined){
                b_obj[str2[i]+str2[i+1]] = 1;
            } else {
                b_obj[str2[i]+str2[i+1]] += 1;
            };
        };
    };
    let a = Object.assign({}, a_obj); // 합, 얕은복사
    let b = {}; // 교
    for (const [key, value] of Object.entries(b_obj) ){
        // 합집합
        if (a[key] === undefined){
            a[key] = value;
        } else {
            a[key] = Math.max(value, a_obj[key]);
        }
    }
    for (const [key, value] of Object.entries(a)) {
        if (a_obj[key] !== undefined && b_obj[key] !== undefined){
            b[key] = Math.min(a_obj[key], b_obj[key]);
        };
    };
    const aa = Object
        .values(a)
        .reduce((prev, curr)=>{
            return prev + curr;
        },0);
    const bb = Object
        .values(b)
        .reduce((prev, curr) => {return prev+curr},0);    
    if (aa === 0 && bb === 0){
        return number;
    }
    answer = parseInt(bb / aa * number);
    return answer;
};

solution("E=M*C^2", "e=m*c^2");

