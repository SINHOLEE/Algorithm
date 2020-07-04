function jumpingOnClouds(c) {
    const dp = new Array(c.length);
    dp.fill(999);
    dp[0] = 0;
    for(let i=0; i<c.length; i++){
        if (!c[i]){
            if (i === c.length-1) continue;
            if (!c[i+1]) dp[i+1] = Math.min(dp[i+1], dp[i]+1);
            if (i === c.length-2) continue;
            if(!c[i+2]) dp[i+2] = Math.min(dp[i+2], dp[i]+1);
        }
    }
    return dp[c.length-1];
}

jumpingOnClouds([0, 0, 0, 0, 1, 0])