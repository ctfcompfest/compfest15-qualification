function countDiff(str) {
	const target = "650e2014a6d7041d8024a8984e47cc9810cead06b0c24dfc742aa71c6de29cb42679b1544286ed09cbf2d2bebd7c2ccd1148";
	var count = 0
	for (let i = 0; i < 100; i+=2) {
  		if (!str.substring(i, i+2).localeCompare(target.substring(i, i+2))) {
  			count += 1;
  		}
	}
	return count;
}
Java.perform(function() {
    Java.use("com.ivanox.godroid.MainActivity").onCreate.implementation = function(b) {
    	this.onCreate(b);
    	console.log("halo");
    	var utils = Java.use("utils.Utils");
    	const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_";
    	var flag = "";
    	var currCount = 0;
    	var temp = "";
    	
    	var count = 0;
    	while (flag.length != 50) {
    		for (let i=0; i<charset.length; i++) {
    			temp = utils.encrypt(flag + charset[i] + "\x01".repeat(50 - flag.length - 1));
    			
			count = countDiff(temp);
			if (count > currCount) {
				currCount = count;
				flag += charset[i];
				console.log(flag);
				break;
			}	
    		}
    	}
    }


});
