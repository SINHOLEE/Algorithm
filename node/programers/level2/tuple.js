// 감상평: 너무 더럽게 풀었다...

function solution(s) {
    const arr = [];
    let flag = 0;
    let idx = 0;
    let num = '';
    for(let i = 0; i < s.length; i++){
        if (s[i] === '{'){
            if (flag === 1){
                arr.push([]);
            }
            flag++
        } else {
            // '}', ',' ,숫자
            if (s[i] === '}'){
                if (flag === 2){
                    arr[idx].push(Number(num));
                    num = '';
                    idx++;
                } 
                flag--
            } else{
                if (s[i] === ','){
                    if (flag === 2){
                        arr[idx].push(Number(num));
                        num = '';
                    }
                } else{
                    // 숫자
                    num += s[i];
                }
            }
        }
    };
    arr.sort((a, b)=>{
        if (a.length < b.length) {
            return -1;
        } else {
            return 1;
        }
    });
    console.log(arr);
    let answer = [];
    let dic = {};
    arr.forEach( obj => {
        let temp_dic = {};
        for (let i = 0; i<obj.length; i++){
            if (temp_dic[obj[i]] === undefined){
                temp_dic[obj[i]] = 1;
            } else{
                temp_dic[obj[i]] += 1;
            };
            if (dic[obj[i]] !== temp_dic[obj[i]]){
                answer.push(obj[i]);
            };
        };
        dic = temp_dic;
    })
    return answer;
}

solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")
