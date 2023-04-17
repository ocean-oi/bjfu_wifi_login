4.2.3.2 url-test 策略组
并发测试所有子策略，选择延迟最低的策略。有以下几个参数

url：用于测试的 URL。
timeout：测试的最长等待时间，超过该时间的策略将标记为失败不再继续等待。
interval：每次测试的间隔时间。所有类 url-test 组的测试时机为：
首次使用时进行测试。
后续使用该策略组时，如果上次测试的时间间隔已大于 interval 设置时间，则再次触发测试。
当目前选中策略产生不可恢复性错误时，直接触发测试。
网络切换后，将清理之前的测试结果，当策略组被使用时触发首次测试。
tolerance：容忍度，如果某几个策略测试结果相差不大，那么会导致在这几个策略中频繁切换，如果策略的代理服务器的出口 IP 不同，可能会触发目标网站的风险控制。所以加入了容忍度设计，仅当新一次的测试结果中，最佳策略比原选中策略的延迟差大于容忍度时，才会切换至新的策略。
evaluate-before-use：默认情况下，在首次使用策略组时将直接使用子策略中的第一个策略，同时触发延迟测试。如果配置了 evaluate-before-use=true，那么首次使用时将等待测试完毕后选择最佳策略。、



配置文件的组成主要分为：`基本设置、服务器信息、服务器分组信息、规则（对应服务器分组）`，各个部分`顺序不可调换`，否则会造成OpenClash功能异常

[Introduce - Clash (gitbook.io)](https://lancellc.gitbook.io/clash/)

[Home · vernesong/OpenClash Wiki · GitHub](https://github.com/vernesong/OpenClash/wiki)