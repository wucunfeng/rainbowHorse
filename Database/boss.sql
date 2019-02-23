CREATE TABLE Boss
(
    jobTitle    CHAR (20) NOT NULL, -- 岗位
    Salary  CHAR (10) NULL, -- 工资
    jobSite     CHAR (30) NULL,  -- 上班地点
    jobExperience CHAR (10) NULL, -- 工作经验
    jobFinancing CHAR (5) NULL, -- 学历
    jobEmployees VARCHAR (1000) NULL, -- 公司人数
    jobRelease   DATE NULL, -- 发布日期
    jobCompany  CHAR(10) NULL
);
