/*
Students and Instructors
Part I

Given the following array of objects:

var students = [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]
Create a program that outputs:

Michael Jordan
John Rosales
Mark Guillen
KB Tonel
*/
var students = [
     {
         first_name:  'Michael',
         last_name : 'Jordan'
     },
     {
         first_name : 'John',
         last_name : 'Rosales'
     },
     {
         first_name : 'Mark',
         last_name : 'Guillen'
     },
     {
         first_name : 'KB',
         last_name : 'Tonel'
     }
];

for (var student in students) {
    console.log(students[student].first_name + " " + students[student].last_name);
}

/*
Part II (Optional)

Now, given the following dictionary:

var users = {
 'Students': [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }
Create a program that prints  the following format (including the number of characters in each combined name):

Students
1 - MICHAEL JORDAN - 13
2 - JOHN ROSALES - 11
3 - MARK GUILLEN - 11
4 - KB TONEL - 7
Instructors
1 - MICHAEL CHOI - 11
2 - MARTIN PURYEAR - 13

*/

var users = {
 'Students': [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }
for (var student in users.Students) {
    console.log(student + " " + users.Students[student].first_name + " " + users.Students[student].last_name + " " + (users.Students[student].first_name.length + users.Students[student].last_name.length));
}