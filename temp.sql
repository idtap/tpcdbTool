SET CLIENT_ENCODING TO UTF8;
SET STANDARD_CONFORMING_STRINGS TO ON;
BEGIN;
CREATE TABLE "test1"."structureline" (gid serial,
"assetgroup" float8,
"assettype" int4,
"creationda" date,
"creator" varchar(254),
"lastupdate" date,
"updatedby" varchar(254),
"globalid" varchar(38),
"assetid" varchar(32),
"capacity" int4,
"dateinstal" date,
"depth" numeric,
"labeltext" varchar(254),
"manufactur" varchar(32),
"material" varchar(128),
"model" varchar(32),
"notes" varchar(254),
"owner" varchar(32),
"serialnumb" varchar(32),
"yearmanufa" float8,
"shape_stle" numeric);
ALTER TABLE "test1"."structureline" ADD PRIMARY KEY (gid);
SELECT AddGeometryColumn('test1','structureline','geom','3857','MULTILINESTRING',4);
COMMIT;
ANALYZE "test1"."structureline";
