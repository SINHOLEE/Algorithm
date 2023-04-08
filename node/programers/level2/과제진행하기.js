//https://school.programmers.co.kr/learn/courses/30/lessons/176962#

const convertTimeToUTC = (time) => {
    const [hour, min] = time.split(":").map(Number);
    return hour * 60 + min;
};

const solution = (plans) => {
    const ANSWER = [];

    const works = [];
    let currentTime = 0;

    const sortedWorks = plans
        .map(([name, start, playTime]) => [parseInt(convertTimeToUTC(start)), { name, playTime:Number(playTime) }])
        .sort(([a], [b]) => a - b);
    for (const [start, { name, playTime }] of sortedWorks) {
        if(works.length){
            while (currentTime < start && works.length > 0) {
                const [workName, restWorkTime] = works.pop();
                if (currentTime + restWorkTime <= start) {
                    ANSWER.push(workName);
                    currentTime += restWorkTime;
                } else {
                    const spentTime = start - currentTime;
                    const remainingTime = restWorkTime - spentTime;
                    works.push([workName, remainingTime]);
                    currentTime = start;
                }
            }
        }
        works.push([name, playTime]);
        // 이걸 초기화 안해서 문제였음

        currentTime = start;

    }

    while (works.length > 0) {
        const [name] = works.pop();
        ANSWER.push(name);
    }

    return ANSWER;
};
