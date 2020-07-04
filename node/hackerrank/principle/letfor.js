function findUser(id, callback){
    setTimeout(() => {
        callback({id:id, name: "사용자 # " +  id})
    }, 1000);
}

function findUsers(ids){
    for(let i in ids){
        console.log(i, ids[i])
        findUser(ids[i], function(user){
            console.log("사용자 id", ids[i]);
            console.log("사용자 정보", user);
        })
    }
}

findUsers([1,23,44,12,1]);