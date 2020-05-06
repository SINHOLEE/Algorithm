function sume_blank(){
    /*
    [1,1,0,0]
    [1,1,1,0]
    [0,1,1,0]
    [0,0,0,0]
    이런 배열을 모두 썸하고, 새로운 빈 배열을 생성한다 이때 새로운 2차배열은 글로벌
    return은 1의 총 합
    */
    let num = 0;
    for(let i=0; i<mm; i++){
        for (let j=0; j<nn; j++){
            num += blank[i][j];
            blank[i][j] = 0;
        }
    }
    return num;
}

function move(){
    /*
    [1,0,0,0]
    [1,1,1,0]
    [0,0,1,0]
    [0,1,0,0]
    */
   
   // 이 배열에서 1인 mat의 원소를 지우고, 
   for (let i = 0; i<mm; i++){
       for( let j = 0; j<nn; j++){
            if(blank[i][j] === 1){
                mat[i][j] = '';
            };
        };
    };
   //각 위치의 빈칸원소를 채운다.
   for(let jj=0; jj<nn; jj++){
      for(let ii = mm-1; ii>=0; ii--){
          if (mat[ii][jj] !== ''){
              let i = ii;
              let j = jj;
              while(true){
                  if (i+1 < mm && mat[i+1][j] ===''){
                     [mat[i][j], mat[i+1][j]] = [mat[i+1][j], mat[i][j]]
                      i = i+1;
                  } else {
                      break;
                  };
              };
          };
      } ;
   };
};


function twobytwo(i, j, value){
    // 현재 위치를 기준으로 모두가 같으면 true, 하나라도 다르면 false 반환
    for(let ii = i; ii<i+2; ii++){
        for (let jj = j; jj<j+2; jj++){
            if (mat[ii][jj] !== value) return false;
        };       
    } ;
    for(let ii = i; ii<i+2; ii++){
        for (let jj = j; jj<j+2; jj++){
            blank[ii][jj] = 1;
        };       
    };
    return true;
   };


function solution(m, n, board) {
    var answer = 0;
    mm = m;
    nn = n;
    mat = Array.from(Array(m), ()=> Array(n));
    blank = Array.from(Array(m), ()=> Array(n));
    for (let i = 0; i<m; i++){
        for( let j = 0; j<n; j++){
            mat[i][j] = board[i][j];
            blank[i][j] = 0;
        };
    };
    // 
    while (true){
        let flag = true;
        for(let i=0; i<m-1; i++){
            for(let j=0;j<n-1; j++){
                // 이중포문을 돌면서 2*2가 같으면 지울거 체크 => 새로운 배열 필요
                if(mat[i][j] !== '' && twobytwo(i, j, mat[i][j])){
                    flag = false;
                }
            }
        }
        // 사라진 원소를 기준으로 move함수 실행
        move();
        // 사라질 원소의 배열은 0 0 0 1 1 이런식으로 되어있으므로 초기화 하기 전에 sum sum해서 answer관리
        answer += sume_blank();
        // 이 짓을 2*2 체크 하면서 while문을 돌릴건데 2*2가 한번도 없을때 멈춘다
        if(flag) break;
    }
    return answer;
}

let mm = 0;
let nn = 0;
let mat = [];
let blank = [];
solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])


