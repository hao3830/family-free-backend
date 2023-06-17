
CREATE DATABASE IF NOT EXISTS se_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE se_db;

SET NAMES utf8mb4;
SET CHARACTER SET utf8mb4;

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
    MAQUEQUAN VARCHAR(50) NOT NULL,
    MANGHENGHIEP VARCHAR(50) NOT NULL,
    DIACHI VARCHAR(100) NOT NULL,
    MATHANHVIENCU VARCHAR(50),
    MALOAIQUANHE VARCHAR(50),
    NGAYPHATSINH DATETIME  NOT NULL ,
    THEHE INT NOT NULL,


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
    MANGUYENNHAN VARCHAR(50) NOT NULL,
    MADIADIEMMAITANG VARCHAR(50) NOT NULL,
    MATHANHVIEN VARCHAR(50) NOT NULL,

    PRIMARY KEY(MAKETTHUC),
    FOREIGN KEY (MANGUYENNHAN) REFERENCES NGUYENNHAN(MANGUYENNHAN),
    FOREIGN KEY (MADIADIEMMAITANG) REFERENCES DIADIEMMAITANG(MADIADIEMMAITANG),
    FOREIGN KEY (MATHANHVIEN) REFERENCES THANHVIEN(MATHANHVIEN)
);

CREATE TABLE IF NOT EXISTS LOAITHANHTICH (
    MALOAITHANHTICH VARCHAR(50) NOT NULL,
    TENLOAITHANHTICH VARCHAR(50) NOT NULL,

    PRIMARY KEY(MALOAITHANHTICH)
);

CREATE TABLE IF NOT EXISTS BAOCAOTHANHTICH (
    MABAOCAOTHANHTICH VARCHAR(50) NOT NULL,
    NAM INT NOT NULL,
    MALOAITHANHTICH VARCHAR(50) NOT NULL,
    SOLUONGTHANHTICH INT NOT NULL,

    PRIMARY KEY(MABAOCAOTHANHTICH),
    FOREIGN KEY (MALOAITHANHTICH) REFERENCES LOAITHANHTICH(MALOAITHANHTICH)
);


CREATE TABLE IF NOT EXISTS THANHTICH (
    MATHANHTICH VARCHAR(50) NOT NULL,
    HOVATEN VARCHAR(50) NOT NULL,
    MALOAITHANHTICH VARCHAR(50) NOT NULL,
    NGAYPHATSINH DATETIME  NOT NULL,
    MATHANHVIEN VARCHAR(50) NOT NULL,

    PRIMARY KEY(MATHANHTICH),
    FOREIGN KEY (MALOAITHANHTICH) REFERENCES LOAITHANHTICH(MALOAITHANHTICH),
    FOREIGN KEY (MATHANHVIEN) REFERENCES THANHVIEN(MATHANHVIEN)

);



INSERT INTO QUEQUAN(MAQUEQUAN, TENQUANHE) VALUES('01', 'TP.HCM');
INSERT INTO QUEQUAN(MAQUEQUAN, TENQUANHE) VALUES('02', 'Hà Nội');
INSERT INTO QUEQUAN(MAQUEQUAN, TENQUANHE) VALUES('03', 'Đà Nẵng');
INSERT INTO QUEQUAN(MAQUEQUAN, TENQUANHE) VALUES('04', 'Quảng Ngãi');
INSERT INTO QUEQUAN(MAQUEQUAN, TENQUANHE) VALUES('05', 'Quảng Nam');
INSERT INTO QUEQUAN(MAQUEQUAN, TENQUANHE) VALUES('06', 'Huế');
INSERT INTO QUEQUAN(MAQUEQUAN, TENQUANHE) VALUES('07', 'Bình Định');


INSERT INTO NGHENGHIEP(MANGHENGHIEP, TENNGHENGHIEP) VALUES('EG', 'Engineer');
INSERT INTO NGHENGHIEP(MANGHENGHIEP, TENNGHENGHIEP) VALUES('DC', 'Doctor');
INSERT INTO NGHENGHIEP(MANGHENGHIEP, TENNGHENGHIEP) VALUES('FM', 'Famer');
INSERT INTO NGHENGHIEP(MANGHENGHIEP, TENNGHENGHIEP) VALUES('IL', 'Illutrator');
INSERT INTO NGHENGHIEP(MANGHENGHIEP, TENNGHENGHIEP) VALUES('SG', 'Singer');
INSERT INTO NGHENGHIEP(MANGHENGHIEP, TENNGHENGHIEP) VALUES('DR', 'Drawer');
INSERT INTO NGHENGHIEP(MANGHENGHIEP, TENNGHENGHIEP) VALUES('CS', 'CS-er');


INSERT INTO QUANHE(MALOAIQUANHE, TENLOAIQUANHE) VALUES('01', 'Con');
INSERT INTO QUANHE(MALOAIQUANHE, TENLOAIQUANHE) VALUES('02', 'Vợ / Chồng');
-- INSERT INTO QUANHE(MALOAIQUANHE, TENLOAIQUANHE) VALUES('03', 'Ly thân');
-- INSERT INTO QUANHE(MALOAIQUANHE, TENLOAIQUANHE) VALUES('04', 'Kết hôn');
-- INSERT INTO QUANHE(MALOAIQUANHE, TENLOAIQUANHE) VALUES('05', 'Có nhiều mối quan hệ');
-- INSERT INTO QUANHE(MALOAIQUANHE, TENLOAIQUANHE) VALUES('06', 'Mập mờ');
-- INSERT INTO QUANHE(MALOAIQUANHE, TENLOAIQUANHE) VALUES('07', 'Hẹn hò');


INSERT INTO NGUYENNHAN(MANGUYENNHAN, TENNGUYENNHAN) VALUES('01', 'Tai nạn');
INSERT INTO NGUYENNHAN(MANGUYENNHAN, TENNGUYENNHAN) VALUES('02', 'Tự sát');
INSERT INTO NGUYENNHAN(MANGUYENNHAN, TENNGUYENNHAN) VALUES('03', 'Ám sát');
INSERT INTO NGUYENNHAN(MANGUYENNHAN, TENNGUYENNHAN) VALUES('04', 'Mưu sát');
INSERT INTO NGUYENNHAN(MANGUYENNHAN, TENNGUYENNHAN) VALUES('05', 'Bệnh tật');
INSERT INTO NGUYENNHAN(MANGUYENNHAN, TENNGUYENNHAN) VALUES('06', 'Hi sinh');
INSERT INTO NGUYENNHAN(MANGUYENNHAN, TENNGUYENNHAN) VALUES('07', 'Ngu thì chết');


INSERT INTO DIADIEMMAITANG(MADIADIEMMAITANG, TENDIADIEMMAITANG) VALUES('01', 'TP.HCM');
INSERT INTO DIADIEMMAITANG(MADIADIEMMAITANG, TENDIADIEMMAITANG) VALUES('02', 'Hà Nội');
INSERT INTO DIADIEMMAITANG(MADIADIEMMAITANG, TENDIADIEMMAITANG) VALUES('03', 'Đà Nẵng');
INSERT INTO DIADIEMMAITANG(MADIADIEMMAITANG, TENDIADIEMMAITANG) VALUES('04', 'Quảng Ngãi');
INSERT INTO DIADIEMMAITANG(MADIADIEMMAITANG, TENDIADIEMMAITANG) VALUES('05', 'Quảng Nam');
INSERT INTO DIADIEMMAITANG(MADIADIEMMAITANG, TENDIADIEMMAITANG) VALUES('06', 'Huế');
INSERT INTO DIADIEMMAITANG(MADIADIEMMAITANG, TENDIADIEMMAITANG) VALUES('07', 'Bình Định');


INSERT INTO LOAITHANHTICH(MALOAITHANHTICH, TENLOAITHANHTICH) VALUES('01', 'Thế giới');
INSERT INTO LOAITHANHTICH(MALOAITHANHTICH, TENLOAITHANHTICH) VALUES('02', 'Châu lục');
INSERT INTO LOAITHANHTICH(MALOAITHANHTICH, TENLOAITHANHTICH) VALUES('03', 'Quốc gia');
INSERT INTO LOAITHANHTICH(MALOAITHANHTICH, TENLOAITHANHTICH) VALUES('04', 'Khu vực');
INSERT INTO LOAITHANHTICH(MALOAITHANHTICH, TENLOAITHANHTICH) VALUES('05', 'Tỉnh');
INSERT INTO LOAITHANHTICH(MALOAITHANHTICH, TENLOAITHANHTICH) VALUES('06', 'Huyện');
INSERT INTO LOAITHANHTICH(MALOAITHANHTICH, TENLOAITHANHTICH) VALUES('07', 'Địa phương');

