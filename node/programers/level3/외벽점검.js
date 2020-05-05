// function perm()
function make_falselist(m) {
    let lis = new Array(m);
    for (let i = 0; i<m; i++){
        lis[i] = false;
    }
    return lis;
}

function point_round(cur_point, lis){
    
    let n = 0; // n === weak_cnt 일때, i+1을 반환해서 
    let i = 0;
    let next_point = 0;
    let temp = 0; // 이동거리
    check_weak = make_falselist(weak_cnt);
    for (i = 0; i<dist_cnt; i++){
        temp = 0;
        while (true){
            if (temp > lis[i]) break;
            if (check_weak[cur_point]) break;
            check_weak[cur_point] = true;
            next_point = (cur_point + 1) % weak_cnt;
            n++
            if (cur_point === weak_cnt-1) {  // weak_cnt - 1 이거 까먹지 말자 진짜;
                temp += (global_n - global_weak[weak_cnt-1] + global_weak[0]);
            } else {
                temp += global_weak[next_point] - global_weak[cur_point]; 
            }
            cur_point = next_point;
        }
        
        
        // 만약 넥스트 포인트까지 갈 수 있으면 간다
        // 갔는데 check_weak가 true이면 브레이크, 아니면 쭉 진행
        if (n === weak_cnt){
            let r = i+1;
            return i+1;
            
        } 

    }
    return 9; // 전부다 못 고치는 경우
}


function find_min_value(lis){
    let n = 9;
    for (let i = 0; i<weak_cnt; i++){
        n = Math.min(point_round(i, lis), n);
    }
    return n;
}


function perm( depth, lis){
    if (depth === dist_cnt){
        answer = Math.min(answer, find_min_value(lis));
        // 여기서 뭔가를 해
        return 
    }
    for(let i = 0; i< dist_cnt; i++){
        if(perm_visited[i] === true) continue;
        perm_visited[i] = true;
        perm(depth+1, lis.concat(global_dist[i]));
        perm_visited[i] = false;
    }
}


function solution(n, weak, dist) {
    global_dist = dist;
    global_weak = weak;
    global_n = n;
    weak_cnt = weak.length;
    dist_cnt = dist.length;
    perm_visited = make_falselist(dist_cnt);
    perm(0,[]);
    if (answer === 9){
        return -1;
    } else {
        return answer;
    }
}
let global_dist = [];
let global_weak = [];
let global_n = 0;
let answer = 9;
let perm_visited = [];
let check_weak = [];
let dist_cnt = 0;
let weak_cnt = 0;

const a  = solution(12, [1, 5, 6, 10], [1, 2, 3, 4])
console.log(a);