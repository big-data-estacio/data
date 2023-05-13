package src;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.util.Date;
import java.util.Scanner;

public class User {
    Integer id;
    String phone;
    String address;
    Date timestamp;
    boolean isStaff;
    private boolean inDB = false;

    public User(String phone, Scanner scanner) {

        File file = new File("./data/users.csv");
        Scanner fileScanner;
        try {
            fileScanner = new Scanner(file);
            // process the file, one line at a time
            while (fileScanner.hasNextLine()) {

                // split the line on comma
                String[] line = fileScanner.nextLine().split(",");

                // check is required row is found
                if (line[1].equals(phone)) {
                    // to prevent duplicate records
                    this.inDB = true;
                    // check permissions
                    if (line[4].equals("true")) {
                        this.isStaff = true;
                    }
                    this.address = line[2];
                }

            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        this.id = Utils.getNewId("./data/users.csv");
        this.phone = phone;
        this.address = getOrAddAddress(phone, scanner);
        this.timestamp = new Date();

        addUserToFile(this);
    }

    public String getOrAddAddress(String phone, Scanner scanner) {
        // if user was not found get thier address
        if (this.address != null) {
            return this.address;
        }
        return Utils.getStringInRange("📍 Your Address: ", 1, 100, scanner);
    }

    public void addUserToFile(User user) {
        String data = user.csvString();

        // if user was already found in db
        if (inDB)
            return;
        try {
            FileWriter writer = new FileWriter("./data/users.csv", true);
            writer.write(data);
            writer.write(System.getProperty("line.separator"));
            writer.close();

            this.inDB = true;
        } catch (Exception e) {
            e.getStackTrace();
        }
    }

    public String csvString() {
        return this.id.toString() + "," + this.phone + "," + this.address.toString() + "," + this.timestamp + ","
                + this.isStaff;
    }

}
