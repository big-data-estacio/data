> Open restaurant problem solution, given data in csv format, we need to find open restaurant(s) at a specified date &amp; time.

#### Prerequisites:
- JDK 11


# CSV data samples:

- cliente,horario
- Kushi Tsuru,Mon-Sun 11:30 am - 9 pm"
- Osakaya Restaurant,"Mon-Thu, Sun 11:30 am - 9 pm  / Fri-Sat 11:30 am - 9:30 pm"
- The Stinking Rose,"Mon-Thu, Sun 11:30 am - 10 pm  / Fri-Sat 11:30 am - 11 pm"
- McCormick & Kuleto's,"Mon-Thu, Sun 11:30 am - 10 pm  / Fri-Sat 11:30 am - 11 pm"
- Mifune Restaurant,Mon-Sun 11 am - 10 pm"
- The Cheesecake Factory,Mon-Thu 11 am - 11 pm  / Fri-Sat 11 am - 12:30 am  / Sun 10 am - 11 pm"
- New Delhi Indian Restaurant,Mon-Sat 11:30 am - 10 pm  / Sun 5:30 pm - 10 pm"
- Iroha Restaurant,"Mon-Thu, Sun 11:30 am - 9:30 pm  / Fri-Sat 11:30 am - 10 pm"
- Rose Pistola,Mon-Thu 11:30 am - 10 pm  / Fri-Sun 11:30 am - 11 pm"
- Alioto's Restaurant,Mon-Sun 11 am - 11 pm"
- Canton Seafood & Dim Sum Restaurant,Mon-Fri 10:30 am - 9:30 pm  / Sat-Sun 10 am - 9:30 pm"
- All Season Restaurant,Mon-Fri 10 am - 9:30 pm  / Sat-Sun 9:30 am - 9:30 pm"
- Bombay Indian Restaurant,Mon-Sun 11:30 am - 10:30 pm"
- Sam's Grill & Seafood Restaurant,Mon-Fri 11 am - 9 pm  / Sat 5 pm - 9 pm"


# Solution:
Building adequate data structer to hold retaurant working days / hours:
Ex:
````
Restaurant-Name: {
  DayOfWeek(Sunday): {
    Pair(start time, closing time),//first shift on a specified date.
    Pair(start time, closing time),//first shift on a specified date.
    //....
  },
   DayOfWeek(Monday): {
    Pair(11:30 AM, 12:00 AM),//first shift on a specified date.
    Pair(00 AM, 2:00 OM),//first shift on a specified date.
  },
  //....
}
````


# Execute:
> Java -jar target/open-resturant-1.0-SNAPSHOT.jar  /{location}/target/test-classes/rest_hours.csv" csv" "2019-01-01 10:10 PM"
