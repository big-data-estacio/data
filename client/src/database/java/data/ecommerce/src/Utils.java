package src;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.Vector;
import java.io.File;
import java.math.BigInteger;

public class Utils {

    public static void showOptions(Vector<String> options) {
        // create a vector to store valid options ids
        Vector<Integer> validOptions = new Vector<>(options.size());

        List<List<String>> rows = new ArrayList<>();
        List<String> headers = Arrays.asList("|", "Option", "|", "Task");
        rows.add(headers);
        for (int i = 0; i < options.size(); i++) {
            validOptions.add(i + 1);
            rows.add(Arrays.asList("|", Integer.toString(i + 1) + ".", "|", options.get(i)));
        }

        System.out.println(Print.formatAsTable(rows, Print.PURPLE, Print.CYAN));
    }

    public static int getOption(Vector<String> options, Scanner scanner) {
        Vector<Integer> validOptions = new Vector<>(options.size());

        Print.print("");
        for (int i = 0; i < options.size(); i++) {
            validOptions.add(i + 1);
        }
        return getIntInRange(Print.GREEN + "Your Choice: " + Print.RESET, 1, validOptions.size(), scanner);
    }

    // getting values
    public static String getStringInRange(String prompt, int minLength, int maxLength, Scanner scanner) {
        String validString = "";
        Print.print(prompt, true);

        while (scanner.hasNext()) {
            validString = scanner.next().toString();
            if (validString.length() <= maxLength && validString.length() >= minLength) {
                break;
            } else {
                Print.print("❗️ Invalid input String. Try again...", Print.RED);
                Print.print(prompt, true);
            }
        }
        return validString;
    }

    public static int getIntInRange(String prompt, int minLength, int maxLength, Scanner scanner) {
        int validInteger = -1;
        Print.print(prompt, true);
        while (scanner.hasNext()) {
            if (scanner.hasNextInt()) {
                validInteger = scanner.nextInt();
                if (String.valueOf(validInteger).length() <= maxLength
                        && String.valueOf(validInteger).length() >= minLength) {
                    break;
                } else {
                    Print.print("❗️ Invalid input integer. Try again...", Print.RED);
                    Print.print(prompt, true);
                }
            } else {
                Print.print("❗️ Invalid input. Must be an integer, try again...", Print.RED);
                Print.print(prompt, true);
                scanner.next();
            }
        }
        return validInteger;
    }

    public static BigInteger getBigIntInRange(String prompt, int minLength, int maxLength, Scanner scanner) {
        BigInteger validInteger = new BigInteger("-1");
        Print.print(prompt, true);
        while (scanner.hasNext()) {
            if (scanner.hasNextBigInteger()) {
                validInteger = scanner.nextBigInteger();

                if (String.valueOf(validInteger).length() <= maxLength
                        && String.valueOf(validInteger).length() >= minLength) {
                    break;
                } else {
                    Print.print("❗️ Invalid input integer. Try again...", Print.RED);
                    Print.print(prompt, true);
                }
            } else {
                Print.print("❗️ Invalid input. Must be an integer, try again...", Print.RED);
                Print.print(prompt, true);
                scanner.next();
            }
        }
        return validInteger;
    }

    public static Double getDoubleInRange(String prompt, Double minLength, Double maxLength, Scanner scanner) {
        Double validDouble = -1.00;
        Print.print(prompt, true);
        while (scanner.hasNext()) {
            if (scanner.hasNextDouble()) {
                validDouble = scanner.nextDouble();
                if (String.valueOf(validDouble).length() <= maxLength
                        && String.valueOf(validDouble).length() >= minLength) {
                    break;
                } else {
                    Print.print("❗️ Invalid input double. Try again...", Print.RED);
                    Print.print(prompt, true);
                }
            } else {
                Print.print("❗️ Invalid input. Must be an double, try again...", Print.RED);
                Print.print(prompt, true);
                scanner.next();
            }
        }
        Print.print("", true);
        return validDouble;
    }

    // file management
    public static int getNewId(String fileName) {
        // try {
        // return Files.lines(new File(fileName).toPath(),
        // Charset.defaultCharset()).count() + 1;
        // } catch (Exception e) {
        // e.getStackTrace();
        // }
        // return 100000;
        File file = new File(fileName);
        String[] lastRow = LastLine.tail(file).split(",");
        try {
            int lastId = Integer.parseInt(lastRow[0]);
            return lastId + 1;
        } catch (Exception e) {
            return 1;
        }
    }

}
