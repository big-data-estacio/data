package src;

import java.util.Scanner;
import java.util.Vector;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;


public class Products {
    Vector<Product> products = new Vector<>();

    /**
     * on instantiation loads data from 'products.csv' to a vector called 'products'
     * in the class
     **/
    Products() {
        File file = new File("./data/products.csv");
        Scanner fileScanner;
        try {
            fileScanner = new Scanner(file);
            // process the file, one line at a time
            while (fileScanner.hasNextLine()) {
                String[] line = fileScanner.nextLine().split(",");
                if (line[4].equals("true")) {
                    Product product = new Product(
                                        Integer.parseInt(line[0]), 
                                        line[1], 
                                        Double.parseDouble(line[2]),
                                        line[3]);
                    this.products.add(product);
                }
            }
            fileScanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    public Vector<Product> getProducts() {
        return this.products;
    }

    public Product productIdToProduct(int productId) {
        for (Product product: products) {
            if (product.id == productId) {
                return product;
            }
        }
        return null;
    }

    public void addProduct(Scanner scanner) {
        int id = Utils.getNewId("./data/products.csv");
        String name = Utils.getStringInRange("Product Name: ", 1, 30, scanner);
        Double price = Utils.getDoubleInRange("Product Price: ", 1.0, 1000.0, scanner);
        String description = Utils.getStringInRange("Product Description: ", 1, 100, scanner);

        Product product = new Product(id, name, price, description);
        this.products.add(product);
        addProductToFile(product);
    }

    public void addProductToFile(Product product) {
        String data = product.csvString();
        try {
            // Creates a Writer using FileWriter
            FileWriter writer = new FileWriter("./data/products.csv", true);
            // Writes string and line seperator to the file
            writer.write(data);
            writer.write(System.getProperty("line.separator"));
            // Closes the writer
            writer.close();
        } catch (Exception e) {
            e.getStackTrace();
        }
    }

    
}

class Product {
    Integer id;
    String name;
    Double price;
    String description;
    boolean isActive = true;

    Product(Integer id, String name, double price, String description) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.description = description;
    }

    public String toString() {
        return "ID: " + this.id.toString() + "\n" + "Name: " + this.name + "\n" + "Price: " + this.price.toString()
                + "\n" + "Description: " + this.description.toString();
    }

    public String csvString() {
        return this.id.toString() + "," + this.name + "," + this.price.toString() + "," + this.description + ","
                + this.isActive;
    }
}
