# open_restaurant
Open restaurant problem solution, given data in csv format, we need to find open restaurant(s) at a specified date &amp; time.

> Prerequisites:
- JDK 11

# CSV data samples:

- San Dong House,Mon-Sun 11 am - 11 pm,,,
- Thai Stick Restaurant,Mon-Sun 11 am - 1 am,,,
- Cesario's,"Mon-Thu, Sun 11:30 am - 10 pm  / Fri-Sat 11:30 am - 10:30 pm",,,
- Colombini Italian Cafe Bistro,Mon-Fri 12 pm - 10 pm  / Sat-Sun 5 pm - 10 pm,,,
- Sabella & La Torre,"Mon-Thu, Sun 10 am - 10:30 pm  / Fri-Sat 10 am - 12:30 am",,,
- Soluna Cafe and Lounge,Mon-Fri 11:30 am - 10 pm  / Sat 5 pm - 10 pm,,,
- Tong Palace,Mon-Fri 9 am - 9:30 pm  / Sat-Sun 9 am - 10 pm,,,
- India Garden Restaurant,Mon-Sun 10 am - 11 pm,,,
- Sapporo-Ya Japanese Restaurant,Mon-Sat 11 am - 11 pm  / Sun 11 am - 10:30 pm,,,
- Santorini's Mediterranean Cuisine,Mon-Sun 8 am - 10:30 pm,,,
- Kyoto Sushi,Mon-Thu 11 am - 10:30 pm  / Fri 11 am - 11 pm  / Sat 11:30 am - 11 pm  / Sun 4:30 pm - 10:30 pm,,,
- Marrakech Moroccan Restaurant,Mon-Sun 5:30 pm - 2 am,,,

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
