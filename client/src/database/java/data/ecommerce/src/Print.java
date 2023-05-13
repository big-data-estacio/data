package src;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.Vector;

public class Print {
    // ANSI codes: https://stackoverflow.com/a/5762502/14225169
    public static final String RESET = "\u001B[0m";
    public static final String RED = "\u001B[31m";
    public static final String GREEN = "\u001B[32m";
    public static final String YELLOW = "\u001B[33m";
    public static final String PURPLE = "\u001B[35m";
    public static final String CYAN = "\u001B[36m";
    // public static final String BLACK = "\u001B[30m";
    // public static final String BLUE = "\u001B[34m";

    // handle printing to console using method overloading
    public static void print(String printThis, boolean noNewLine) {
        if (noNewLine) {
            System.out.print(printThis);
        }
    }

    public static void print(String printThis) {
        System.out.println(printThis);
    }

    public static void print(String printThis, String color) {
        System.out.println(color + printThis + RESET);
    }

    public static void print(Integer printThis) {
        System.out.println(printThis);
    }

    public static void print(Vector<Product> printThis, Double cartTotal) {
        List<List<String>> rows = new ArrayList<>();
        List<String> headers = Arrays.asList("|", "ID", "|", "Name", "|", "Price", "|", "Quantity", "|", "Description");
        rows.add(headers);

        // keep track of elements we've already seen
        // (https://stackoverflow.com/a/10457632/14225169)
        Set<List<String>> productCache = new HashSet<List<String>>();

        for (Product element : printThis) {
            int occurrences = Collections.frequency(printThis, element);

            List<String> toAdd = Arrays.asList("|", Integer.toString(element.id), "|", (element.name), "|",
                    "₹" + Double.toString(element.price), "|", Integer.toString(occurrences), "|",
                    (element.description));

            if (productCache.contains(toAdd)) {
                continue;
            } else {
                rows.add(toAdd);
                productCache.add(toAdd);
            }
        }
        rows.add(Arrays.asList("|", "", "|", "", "|", "", "|", "", "|", ""));
        rows.add(Arrays.asList("|", "Total: ", "|", "", "|", "₹" + Double.toString(cartTotal), "|", " ", "|", ""));

        System.out.println(Print.formatAsTable(rows, Print.PURPLE, Print.YELLOW));
    }

    public static void print(Vector<Product> printThis) {
        List<List<String>> rows = new ArrayList<>();
        List<String> headers = Arrays.asList("|", "ID", "|", "Name", "|", "Price", "|", "Description");
        rows.add(headers);

        for (Product element : printThis) {
            List<String> toAdd = Arrays.asList("|", Integer.toString(element.id), "|", (element.name), "|",
                    "₹" + Double.toString(element.price), "|", (element.description));
            rows.add(toAdd);
        }

        System.out.println(Print.formatAsTable(rows, Print.PURPLE, Print.YELLOW));
    }

    public static void printOrders(Vector<Order> printThis) {
        List<List<String>> rows = new ArrayList<>();
        List<String> headers = Arrays.asList("|", "ID", "|", "User", "|", "Products", "|", "Date Ordered");
        rows.add(headers);

        for (Order element : printThis) {
            // empty vector
            Vector<String> vector = new Vector<>();

            // fill vector with info
            for (Product e : element.products) {
                int occurrences = Collections.frequency(element.products, e);
                // vector.add("ID:" + e.id + ", " + e.name + " x" + occurrences + "; ");
                vector.add("Product Id:" + e.id +  " x " + occurrences + "; ");
            }

            // credits: https://stackoverflow.com/a/3042606/14225169
            Set<String> set = new HashSet<String>();
            set.addAll(vector);
            vector.clear();
            vector.addAll(set);
            String joined = String.join("", vector);

            rows.add(Arrays.asList("|", Integer.toString(element.id), "|", element.user.phone, "|", joined, "|",
                    element.dateOrdered));
        }

        System.out.println(Print.formatAsTable(rows, Print.PURPLE, Print.YELLOW));
    }

    public static String getDashes(int numOfDash) {
        String dashes = "";
        for (int i = 0; i < numOfDash; i++) {
            dashes += "-";
        }
        return dashes;
    }

    // modified version of https://stackoverflow.com/a/50649715/14225169
    public static String formatAsTable(List<List<String>> rows, String headerColor, String color) {
        int[] maxLengths = new int[rows.get(0).size()];
        for (List<String> row : rows) {
            for (int i = 0; i < row.size(); i++) {
                maxLengths[i] = Math.max(maxLengths[i], row.get(i).length());
            }
        }

        StringBuilder formatBuilder = new StringBuilder();
        for (int maxLength : maxLengths) {
            formatBuilder.append("%-").append(maxLength + 2).append("s");
        }
        String format = formatBuilder.toString();

        StringBuilder result = new StringBuilder();
        int reqDashes = String.format(format, rows.get(0).toArray()).length() + 1;

        result.append(headerColor);
        result.append(getDashes(reqDashes)).append("\n");

        for (List<String> row : rows) {
            if (rows.indexOf(row) == 0) {
                result.append(String.format(format, row.toArray())).append("|").append("\n");
                result.append(RESET);
                result.append(color);
            } else {
                result.append(String.format(format, row.toArray())).append("|").append("\n");
            }
        }

        result.append(getDashes(reqDashes));
        result.append(RESET);

        return result.toString();
    }
}
