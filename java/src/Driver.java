package src;

import java.util.Scanner;
import java.util.Vector;

public class Driver {
    static User user;
    static Order order;
    static Orders orders;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useDelimiter("\n");

        Vector<String> options = new Vector<>();

        // authentication
        options.add("Login");

        // no auth req
        options.add("Show Products Catalogue");

        // auth required
        options.add("Add To Cart");
        options.add("View Your Cart");
        options.add("Order Now");

        // admin
        options.add("Add New Product To Catalogue");
        options.add("View All Completed Orders");
        options.add("View Completed Order Cart");

        // utils (no auth req)
        options.add("See options");
        options.add("Exit");

        Products products = new Products();
        Utils.showOptions(options);
        boolean flag = true;
        while (flag) {
            int caseChosen = Utils.getOption(options, scanner);

            switch (caseChosen) {
            case 1:
                // Login
                authenticateUser(scanner);
                break;

            case 2:
                // show all products
                Print.print(products.getProducts());
                break;

            case 3:
                // add product to cart
                if (order != null) {
                    Product selectedProduct = null;
                    while (selectedProduct == null) {
                        int productId = Utils.getIntInRange("Add to cart, Product ID: ", 1, 10000, scanner);
                        selectedProduct = products.productIdToProduct(productId);
                        if (selectedProduct != null) {
                            Print.print(selectedProduct.name + " Added to cart ✅", Print.GREEN);
                        } else {
                            Print.print("Invalid Product ID, try again...", Print.RED);
                        }
                    }
                    order.addToCart(selectedProduct);
                } else {
                    Print.print("Login to explore this feature...", Print.YELLOW);
                }
                break;

            case 4:
                // view your cart
                if (order != null) {
                    order.getCartItems();
                } else {
                    Print.print("Login to explore this feature...", Print.YELLOW);
                }
                break;

            case 5:
                // order
                if (order != null) {
                    order.completeOrder(scanner);
                } else {
                    Print.print("Login to explore this feature...", Print.YELLOW);
                }
                break;

            case 6:
                // add product to catalouge
                if (user == null) {
                    Print.print("Login to explore this feature...", Print.YELLOW);
                } else if (user.isStaff) {
                    products.addProduct(scanner);
                } else {
                    Print.print("You do not have permission to add products.", Print.YELLOW);
                }
                break;

            case 7:
                // Print all completed orders (admin only)
                if (user == null) {
                    Print.print("Login to explore this feature...", Print.YELLOW);
                } else if (user.isStaff) {
                    Orders useOrders = getOrCreateOrders();
                    Vector<Order> ord = useOrders.getAllOrders();
                    Print.printOrders(ord);
                } else {
                    Print.print("You do not have permission to view all Orders.", Print.YELLOW);
                }

                break;

            case 9:
                // show options
                Utils.showOptions(options);
                break;

            case 8:
                // view order details
                if (user == null) {
                    Print.print("Login to explore this feature...", Print.YELLOW);
                } else if (user.isStaff) {
                    Orders useOrders1 = getOrCreateOrders();
                    int orderId = Utils.getIntInRange("Order ID: ", 1, 100, scanner);
                    useOrders1.printCartOf(orderId);
                } else {
                    Print.print("You do not have permission to view order details.", Print.YELLOW);
                }
                break;

            default:
                flag = false;
                break;
            }

        }
        scanner.close();
    }

    public static void authenticateUser(Scanner scanner) {
        // get phone number from user
        String userPhone = "" + Utils.getBigIntInRange("📞 Phone: ", 10, 10, scanner);

        // initiate the PhoneOtp class
        PhoneOtp phoneOtp = new PhoneOtp(userPhone);

        // generate otp
        phoneOtp.generateOtp();

        while (true) {
            // get otp from user
            String userOtp = Integer.toString(Utils.getIntInRange("🔑 OTP: ", 6, 6, scanner));

            // validate otp
            if (phoneOtp.validateOtp(userPhone, userOtp)) {
                user = new User(userPhone, scanner);
                order = new Order(user);

                Print.print("Logged In ✅", Print.GREEN);
                return;
            }
            Print.print("❗️ Incorrect OTP. Try again...", Print.RED);
        }
    }

    public static Orders getOrCreateOrders() {
        if (orders != null) {
            return orders;
        }
        Orders createOrders = new Orders();
        orders = createOrders;
        return orders;
    }

}
