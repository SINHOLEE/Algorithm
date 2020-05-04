function solution(participant, completion) {
    var dic = completion.reduce((obj, t)=> {
        console.log(obj, t)
        return (obj[t]= obj[t] ? obj[t]+1 : 1 , obj)
    } ,{});
    console.log(dic)    
    
    return null;
}


solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])



