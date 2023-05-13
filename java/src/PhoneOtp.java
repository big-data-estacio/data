package src;

import java.util.Random;

import java.io.FileNotFoundException;
import java.io.PrintWriter;

public class PhoneOtp {
    private String phone;
    private String otp;

    public PhoneOtp(String phone) {
        this.phone = phone;
    }

    public boolean generateOtp() {
        return sendOtp(getOtp());
    }

    public boolean validateOtp(String phone, String otp) {
        if (this.otp.equals(otp) && this.phone.equals(phone)) {
            return true;
        }
        return false;
    }

    private static String getOtp() {
        Random rand = new Random();
        int number = (rand.nextInt(1000000));
        if (number < 100000) {
            number = (rand.nextInt(1000000)) + 100000;
        }
        return String.format("%06d", number);
    }

    private boolean sendOtp(String otp) {
        this.otp = otp;

        // make API request to otp provider
        // create/update a file 'otp.csv' and print inside it 'phone,otp'
        try (PrintWriter writer = new PrintWriter("./data/otp.csv")) {
            writer.write(phone + ',' + otp);
        } catch (FileNotFoundException e) {
            System.out.println(e);
            return false;
        }
        return true;
    }

}
