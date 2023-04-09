//https://school.programmers.co.kr/learn/courses/30/lessons/150368
//9:05 ->9:50
//목표
// 1 이모티콘 플러스 서비스가입자 늘리기
// 2 판매액 최대 늘리기

// 사용자가 사용하는 기준
// 일정 비율 이상 할인하는 이모티콘 모두 구매
// 이모티콘 구매 비용의 합이 일정가격 이상이 되면 구매했던 모든 이모티콘을 취소하고 이모티콘 플러스에 가입함

// 이모티콘당 할인율을 4개의 경우의수로 나눠서 계산하도록 한다.

const perm = (n)=>{
    const ans = []
    const discounts = [10,20,30,40]
    const _perm = (depth,res,ans)=>{
        if(depth===0){
            ans.push(res)
            return
        }
        for(let i = 0; i<4; i++){
            _perm(depth-1,[...res,discounts[i]],ans)
        }

    }

    _perm(n,[],ans)
    return ans
}
const calcRevenue = (user,discountAndPrice)=>{
    return discountAndPrice.filter(([discount])=>discount>=user[0]).reduce((acc,cur)=>acc+cur[1],0)
}

const calcIsEmoticonPlusUser = (user,discountAndPrice)=>{
    return calcRevenue(user,discountAndPrice) >= user[1]
}

const calcEmotionPlusUserCntAndRevenue = (users,discountAndPrice)=>{
    let emoticonPlusCnt = 0
    let totalRevenue = 0
    for(const user of users){
        if(calcIsEmoticonPlusUser(user,discountAndPrice)){
            emoticonPlusCnt++
        }else{
            totalRevenue+=calcRevenue(user,discountAndPrice)
        }
    }
    return [emoticonPlusCnt,totalRevenue]
}
function solution(users, emoticons) {

    var answer = [];
    const permDiscounts = perm(emoticons.length)
    for (const discountList of permDiscounts){

        const discountAndPrice = []
        for(let i=0; i<emoticons.length; i++){
            discountAndPrice.push([discountList[i],emoticons[i] * ((100 -discountList[i]))/100])
        }

        answer.push(calcEmotionPlusUserCntAndRevenue(users,discountAndPrice))
    }


    return answer.sort((a,b)=>{
        if(a[0]===b[0]){
            return b[1]-a[1]
        }
        return b[0]-a[0]

    })[0];
}