function check(account, bank){
    if (bank[account] === undefined){
        return false;
    }
    return true;
}

function solution(reqs){
    let answer = [];
    let bank = {};
    for (let i = 0; i<reqs.length; i++){
        let req = reqs[i].split(" ");
        let order = req[0];
        let account = req[1];
        let currency = parseInt(req[2]);
        if (order === 'CREATE'){ // 생성
            if (check(account, bank)){
                answer.push(403);
            } else{
                bank[account] = {'balance': 0, 'maxWithdraw': -1 * currency};
                answer.push(200);
            }
        } else if (order === 'DEPOSIT'){
            if( !check(account, bank)){
                answer.push(404);
            } else {
                bank[account]['balance'] += currency;
                answer.push(200);

            }
        }  else { // withDraw
            if( !check(account, bank)){
                answer.push(404);
            } else if ((bank[account]['maxWithdraw'] - bank[account]['balance']) *-1 < currency){
                answer.push(403)
            } else{
                bank[account]['balance'] -= currency;
                answer.push(200);
            }
        }
    }
    console.log(answer)
    return answer;
}

console.log([404, 200, 200, 403], solution(		["DEPOSIT 3a 10000", "CREATE 3a 300000", "WITHDRAW 3a 150000", "WITHDRAW 3a 150001"]));

console.log([200, 403, 200], solution(	["CREATE 3a 10000", "CREATE 3a 20000", "CREATE 2bw 30000", "WITHDRAW 3a 9999", "WITHDRAW 3a 2"]));
