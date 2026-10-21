-- Metadata-driven ingestion configuration used by PL_Metadata_Driven_Ingestion.
-- Run in the database connected to LS_AzureSQL_Metadata.
IF OBJECT_ID('dbo.IngestionMetadata','U') IS NULL
BEGIN
    CREATE TABLE dbo.IngestionMetadata
    (
        EntityName       VARCHAR(50)  NOT NULL PRIMARY KEY,
        RelativeUrl      VARCHAR(100) NOT NULL,
        DestinationPath  VARCHAR(200) NOT NULL,
        IsActive         BIT          NOT NULL DEFAULT 1,
        LoadType         VARCHAR(20)  NOT NULL DEFAULT 'FULL'
    );
END;
GO
IF NOT EXISTS (SELECT 1 FROM dbo.IngestionMetadata WHERE EntityName='customers')
    INSERT INTO dbo.IngestionMetadata(EntityName,RelativeUrl,DestinationPath,IsActive,LoadType)
    VALUES('customers','users','landing/customers',1,'FULL');
IF NOT EXISTS (SELECT 1 FROM dbo.IngestionMetadata WHERE EntityName='orders')
    INSERT INTO dbo.IngestionMetadata(EntityName,RelativeUrl,DestinationPath,IsActive,LoadType)
    VALUES('orders','carts','landing/orders',1,'FULL');
IF NOT EXISTS (SELECT 1 FROM dbo.IngestionMetadata WHERE EntityName='products')
    INSERT INTO dbo.IngestionMetadata(EntityName,RelativeUrl,DestinationPath,IsActive,LoadType)
    VALUES('products','products','landing/products',1,'FULL');
GO
