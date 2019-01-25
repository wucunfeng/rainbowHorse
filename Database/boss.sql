CREATE TABLE Boss
(
    jobTitle    CHAR (20)NOT NULL, -- 岗位
    lowSalary   TINYINT (10)NOT NULL, -- 最低工资
    highSalary  TINYINT (10)NOT NULL, -- 最高工资
    jobSite     CHAR (30)NOT NULL,  -- 上班地点
    jobExperience CHAR (10)NOT NULL, -- 工作经验
    jobFinancing CHAR (5)NOT NULL, -- 学历
    jobEmployees VARCHAR (1000)NOT NULL, -- 公司人数
    jobRelease   DATE NOT NULL, -- 发布日期
    PRIMARY KEY (jobTitle)
);

