let dailyActivities = ["eat", "sleep"];

// add an element at the end
dailyActivities.push("exercise");

console.log(dailyActivities);

// Output: [ 'eat', 'sleep', 'exercise' ]



var arr = [true, 2, 3, "4"];
new_array = arr.reverse()
console.log(new_array);         // ["4", 3, 2, true]

new_array = arr.sort();
console.log(new_array);         // [2, 3, "4", true]

var arr = [1, 2, 3, 4, 10];
console.log(arr.sort());         // [1, 10, 2, 3, 4]
console.log(arr.sort((el1, el2) => el1 - el2)); // [1, 2, 3, 4, 10]
