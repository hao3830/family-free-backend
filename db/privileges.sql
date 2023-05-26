
CREATE DATABASE IF NOT EXISTS se_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS QUEQUAN (
    MAQUEQUAN VARCHAR(50) NOT NULL,
    TENQUANHE VARCHAR(50) NOT NULL,

    PRIMARY KEY (MAQUEQUAN)
);

CREATE TABLE IF NOT EXISTS NGHENGHIEP (
    MANGHENGHIEP VARCHAR(50) NOT NULL,
    TENNGHENGHIEP VARCHAR(50) NOT NULL,

    PRIMARY KEY (MANGHENGHIEP)
);

CREATE TABLE IF NOT EXISTS QUANHE (
    MALOAIQUANHE VARCHAR(50) NOT NULL,
    TENLOAIQUANHE VARCHAR(50) NOT NULL,

    PRIMARY KEY (MALOAIQUANHE)
);

CREATE TABLE IF NOT EXISTS THANHVIEN (
    MATHANHVIEN VARCHAR(50) NOT NULL,
    HOVATEN VARCHAR(50) NOT NULL,
    GIOITINH INT NOT NULL,
    NGAYGIOSINH DATETIME  NOT NULL,
    MAQUEQUAN INT NOT NULL,
    MANGHENGHIEP INT NOT NULL,
    DIACHI VARCHAR(100) NOT NULL,
    MATHANHVIENCU VARCHAR(50),
    MALOAIQUANHE INT NOT NULL,
    NGAYPHATSINH DATETIME  NOT NULL ,


    PRIMARY KEY (MATHANHVIEN),

    FOREIGN KEY (MAQUEQUAN) REFERENCES QUEQUAN(MAQUEQUAN),
    FOREIGN KEY (MANGHENGHIEP) REFERENCES NGHENGHIEP(MANGHENGHIEP),
    FOREIGN KEY (MALOAIQUANHE) REFERENCES QUANHE(MALOAIQUANHE)
);


CREATE TABLE IF NOT EXISTS BAOCAOTANGGIAM (
    MABAOCAOTANGGIAM VARCHAR(50) NOT NULL,
    NAM INT NOT NULL,
    SOLUONGSINH INT NOT NULL,
    SOLUONKETHON INT NOT NULL,
    SOLUONGMAT INT NOT NULL,

    PRIMARY KEY (MABAOCAOTANGGIAM)

);

CREATE TABLE IF NOT EXISTS NGUYENNHAN (
    MANGUYENNHAN VARCHAR(50) NOT NULL,
    TENNGUYENNHAN VARCHAR(50) NOT NULL,

    PRIMARY KEY(MANGUYENNHAN)
);

CREATE TABLE IF NOT EXISTS DIADIEMMAITANG (
    MADIADIEMMAITANG VARCHAR(50) NOT NULL,
    TENDIADIEMMAITANG VARCHAR(50) NOT NULL,

    PRIMARY KEY(MADIADIEMMAITANG)
);


CREATE TABLE IF NOT EXISTS KETTHUC (
    MAKETTHUC VARCHAR(50) NOT NULL,
    HOVATEN VARCHAR(50) NOT NULL,
    NGAYGIOMAT DATETIME  NOT NULL,
    MANGUYENNHAN INT NOT NULL,
    MADIADIEMMAITANG INT NOT NULL,

    PRIMARY KEY(MAKETTHUC),
    FOREIGN KEY (MANGUYENNHAN) REFERENCES NGUYENNHAN(MANGUYENNHAN),
    FOREIGN KEY (MADIADIEMMAITANG) REFERENCES DIADIEMMAITANG(MADIADIEMMAITANG)
);

CREATE TABLE IF NOT EXISTS LOAITHANHTICH (
    MALOAITHANHTICH VARCHAR(50) NOT NULL,
    TENLOAITHANHTICH VARCHAR(50) NOT NULL,

    PRIMARY KEY(MALOAITHANHTICH)
);

CREATE TABLE IF NOT EXISTS BAOCAOTHANHTICH (
    MABAOCAOTHANHTICH VARCHAR(50) NOT NULL,
    NAM INT NOT NULL,
    MALOAITHANHTICH INT NOT NULL,
    SOLUONGTHANHTICH INT NOT NULL,

    PRIMARY KEY(MABAOCAOTHANHTICH),
    FOREIGN KEY (MALOAITHANHTICH) REFERENCES LOAITHANHTICH(MALOAITHANHTICH)
);


CREATE TABLE IF NOT EXISTS THANHTICH (
    MATHANHTICH VARCHAR(50) NOT NULL,
    HOVATEN VARCHAR(50) NOT NULL,
    MALOAITHANHTICH INT NOT NULL,
    NGAYPHATSINH DATETIME  NOT NULL,

    PRIMARY KEY(MATHANHTICH),
    FOREIGN KEY (MALOAITHANHTICH) REFERENCES LOAITHANHTICH(MALOAITHANHTICH)
);





