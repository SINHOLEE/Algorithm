function checkMagazine(magazine, note) {
    let my_map = {};
    let cnt = 0;
    note.forEach(element => {
        if(my_map[element]){
            my_map[element] = my_map[element]+1;
        } else{
            my_map[element] = 1;
        }
        cnt++;
    });
    for(let i=0; i<magazine.length; i++){
        if (my_map[magazine[i]] && my_map[magazine[i]] > 0){
            my_map[magazine[i]] = my_map[magazine[i]]-1;
            cnt--;
        };
    };
    
    console.log(cnt ? "No" : "Yes");
    
}