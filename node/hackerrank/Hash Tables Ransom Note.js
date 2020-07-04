function checkMagazine(magazine, note) {
    const my_map = new Map();
    let cnt = 0;
    note.forEach(element => {
        if(my_map.has(element)){
            my_map.set(element, my_map.get(element)+1);
        } else{
            my_map.set(element, 1);
        }
        cnt = cnt + 1
    });
    magazine.forEach(element=>{
        if(my_map.has(element) && my_map.get(element) >0){
            my_map.set(element, my_map.get(element) - 1);
            cnt--;
        }
    })
    // 오타치지말자 신호야... 
    // for(let i=0; i<magazine.length; i++){
    //     if (my_map.has(magazine[i]) && my_map.get(magazine[i])>0){
    //         my_map.set(magazine[i], my_map.get(magazine[i])-1);  
    //         // 어떻게  my_map.set(magazine[i], my_map.get(magazine[i]-1));이렇게 할 수 가있니 
    //         cnt--;
    //     };
    // };
    
    console.log(cnt ? "No" : "Yes");
    
}

function solve(m,n){
    const magazine = m.split(" ");
    const note = n.split(" ");
    checkMagazine(magazine, note)
}


solve("give me one grand today night", "give one grand today")