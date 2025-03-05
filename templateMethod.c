#include <stdio.h>

// 抽象基类
struct DataProcessor {
    void (*load_data)(void *);
    void (*preprocess_data)(void *);
    void (*analyze_data)(void *);
    void (*save_results)(void *);
    int (*hook)(void *);
};

void process(struct DataProcessor *self, void *context)
{
    self->load_data(context);
    self->preprocess_data(context);
    if (self->hook(context)) {
        self->analyze_data(context);
    }
    self->save_results(context);
}

// CSV处理器
struct CSVDataProcessor {
    struct DataProcessor base; /* 享元，首地址共用 */
    // 可以添加其他CSV处理器特有的成员
};

void csv_load_data(void *context)
{
    printf("Loading data from CSV file\n");
}

void csv_preprocess_data(void *context)
{
    printf("Preprocessing CSV data\n");
}

void csv_analyze_data(void *context)
{
    printf("Analyzing CSV data\n");
}

void csv_save_results(void *context)
{
    printf("Saving results to CSV file\n");
}

int csv_hook(void *context)
{
    return 1;  // 默认执行分析步骤
}

// JSON处理器
struct JSONDataProcessor {
    struct DataProcessor base; /* 享元，首地址共用 */
    // 可以添加其他JSON处理器特有的成员
};

void json_load_data(void *context)
{
    printf("Loading data from JSON file\n");
}

void json_preprocess_data(void *context)
{
    printf("Preprocessing JSON data\n");
}

void json_analyze_data(void *context)
{
    printf("Analyzing JSON data\n");
}

void json_save_results(void *context)
{
    printf("Saving results to JSON file\n");
}

int json_hook(void *context)
{
    return 0;  // 默认不执行分析步骤
}

void init_csv_processor(struct CSVDataProcessor *processor)
{
    processor->base.load_data = csv_load_data;
    processor->base.preprocess_data = csv_preprocess_data;
    processor->base.analyze_data = csv_analyze_data;
    processor->base.save_results = csv_save_results;
    processor->base.hook = csv_hook;
}

void init_json_processor(struct JSONDataProcessor *processor)
{
    processor->base.load_data = json_load_data;
    processor->base.preprocess_data = json_preprocess_data;
    processor->base.analyze_data = json_analyze_data;
    processor->base.save_results = json_save_results;
    processor->base.hook = json_hook;
}

int main()
{
    struct CSVDataProcessor csv_processor;
    struct JSONDataProcessor json_processor;
    printf("%p %p", &csv_processor, &csv_processor.base); /* 享元，首地址共用 */
    init_csv_processor(&csv_processor);
    init_json_processor(&json_processor);

    printf("Processing CSV Data:\n");
    process((struct DataProcessor *)&csv_processor, NULL);

    printf("\nProcessing JSON Data:\n");
    process((struct DataProcessor *)&json_processor, NULL);

    return 0;
}
