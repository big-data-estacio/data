package utils;

import com.opencsv.CSVReader;
import org.apache.commons.codec.digest.DigestUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.lang.NonNull;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Objects;

public class CSVContent {
    private static final Logger LOGGER = LoggerFactory.getLogger(CSVContent.class);

    private List<String[]> fileContent;
    private String fileCheckSum;
    private static final Object lock = new Object();

    public List<String[]> getFileContent() {
        return fileContent;
    }

    private static volatile CSVContent _instance;


    public static CSVContent getInstance(@NonNull String filePath) throws IOException {
        if (_instance == null || !_instance.fileCheckSum.contentEquals(calcCheckSum(filePath))) {
            synchronized (lock) {
                _instance = new CSVContent(filePath);
            }
        }
        return _instance;
    }

    private CSVContent(@NonNull String filePath) throws IOException {
        Objects.requireNonNull(filePath);
        LOGGER.info("reading file: {}", filePath);
        try (var inStream = Files.newInputStream(Paths.get(filePath))) {
            try (var csvReader = new CSVReader(new InputStreamReader(inStream))) {
                fileContent = csvReader.readAll();
                fileCheckSum = DigestUtils.md2Hex(inStream);
            }
        }
    }

    public String getFileCheckSum() {
        return fileCheckSum;
    }

    private static String calcCheckSum(@NonNull String filePath) throws IOException {
        Objects.requireNonNull(filePath);
        LOGGER.info("calc checksum for file: {}", filePath);
        try (InputStream is = Files.newInputStream(Paths.get(filePath))) {
            return DigestUtils.md5Hex(is);
        }
    }
}
