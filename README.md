# 知识图谱相关
### 项目一：Neo4j与python实验测试(neo4j_test)
<!-- wp:heading {"level":3} -->
<h3>安装py2neo</h3>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>为了让python与Neo4j相连，需要安装python中的py2neo库：</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>pip3 install py2neo</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3} -->
<h3>开始实验测试</h3>
<!-- /wp:heading -->

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>本次实验测试主要建立一个有关（购买方，价格，销售方）3元关系的数据库，数据库存储在表格之中。</p></blockquote>
<!-- /wp:quote -->

<!-- wp:paragraph -->
<p>如图所示：</p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":467,"width":484,"height":490,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large is-resized"><img src="https://ripshun.com/wp-content/uploads/2021/03/503ZZDL5J3IL2BL04EH.png" alt="" class="wp-image-467" width="484" height="490"/></figure>
<!-- /wp:image -->

# -----------------------------------------------------

### 项目二： 医疗问答系统
<!-- wp:heading {"level":3} -->
<h3>实验环境</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li>neo4j数据库</li><li>py_aho_corasick模块</li></ul>
<!-- /wp:list -->

<!-- wp:heading {"level":3} -->
<h3>简介</h3>
<!-- /wp:heading -->

<!-- wp:list -->
<ul><li>数据提取模块（从互联网获取数据）</li><li>知识图谱数据库构建模块（将数据清洗构建知识图谱）</li><li>节点匹配模块（匹配节点获取关系）</li><li>问题匹配模块（匹配问题构建查询）</li><li>回答构建模块（输出）</li></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->

<!-- wp:image {"id":475,"width":662,"height":496,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large is-resized"><img src="https://ripshun.com/wp-content/uploads/2021/03/jainjie-1024x769.png" alt="" class="wp-image-475" width="662" height="496"/></figure>
<!-- /wp:image -->

![image](https://user-images.githubusercontent.com/38173291/112132441-97891280-8c05-11eb-96ee-01e32198dda1.png)
![image](https://user-images.githubusercontent.com/38173291/112132456-9ce65d00-8c05-11eb-8fc8-ab6998741d21.png)


# -----------------------------------------------------

### 项目三：哈工大ltp工具包的安装和使用

<!-- wp:quote -->
<blockquote class="wp-block-quote"><p>LTP（Language Technology Platform） 提供了一系列中文自然语言处理工具，用户可以使用这些工具对于中文文本进行分词、词性标注、句法分析等等工作。<br>官方教程：https://github.com/HIT-SCIR/ltp/blob/master/docs/quickstart.rst<br>官方文档：http://ltp.ai/docs/appendix.html</p></blockquote>
<!-- /wp:quote -->

<!-- wp:heading -->
<h2>安装</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>与pyltp不同，ltp4无需安装繁琐的vc环境，也不用考虑python版本对轮子兼容的问题。<br><code>pip install ltp</code></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>在github源代码中可以发现作者主要使用了Electra预训练模型，并使用了transformers库调用模型。所以在安装pyltp之前我们要确保本机上安装的库与ltp中使用的库版本一致，当然如果本机环境并没有安装相应库，安装ltp时会自动安装。</p>
<!-- /wp:paragraph -->

<!-- wp:list -->
<ul><li>torch&gt;=1.2.0</li><li>transformers&gt;=4.0.0, &lt;5.0</li><li>pygtrie&gt;=2.3.0, &lt;2.5</li></ul>
<!-- /wp:list -->

<!-- wp:heading -->
<h2>下载预训练模型参数</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>模型下载地址：https://github.com/HIT-SCIR/ltp/blob/master/MODELS.md<br>在使用ltp时需要选择适合任务大小的模型，将下载下来的压缩文件解压放入文件夹中即可</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2>ltp的使用</h2>
<!-- /wp:heading -->

<!-- wp:heading {"level":4} -->
<h4>加载模型</h4>
<!-- /wp:heading -->

<!-- wp:code -->
<pre class="wp-block-code"><code>ltp = LTP(path='pretrained_model') # 默认加载 Small 模型</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>path中填入模型参数放入的文件夹</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":4} -->
<h4>分句</h4>
<!-- /wp:heading -->


<!-- wp:heading {"level":4} -->
<h4>分词</h4>
<!-- /wp:heading -->


<!-- wp:heading {"level":4} -->
<h4>词性标注</h4>
<!-- /wp:heading -->

<!-- wp:image -->
<figure class="wp-block-image"><img src="https://img-blog.csdnimg.cn/20210325105828836.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NoZW5nc2h1bmhhbmc=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":4} -->
<h4>语义角色标注</h4>
<!-- /wp:heading -->

<!-- wp:image -->
<figure class="wp-block-image"><img src="https://img-blog.csdnimg.cn/20210325105848914.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NoZW5nc2h1bmhhbmc=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":4} -->
<h4>句法分析</h4>
<!-- /wp:heading -->

<!-- wp:image -->
<figure class="wp-block-image"><img src="https://img-blog.csdnimg.cn/20210325105857947.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NoZW5nc2h1bmhhbmc=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"/></figure>
<!-- /wp:image -->


<!-- wp:image -->
<figure class="wp-block-image"><img src="https://img-blog.csdnimg.cn/20210325104454502.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NoZW5nc2h1bmhhbmc=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述"/></figure>
<!-- /wp:image -->

<!-- wp:heading {"level":4} -->
<h4>使用语义角色标注构造关系抽取</h4>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>通过语义角色标注任务可以将句子中各实体以及其关系表示出来，我们以主谓宾关系为例，构建一个（主，谓，宾）的三元组：</p>
<!-- /wp:paragraph -->
