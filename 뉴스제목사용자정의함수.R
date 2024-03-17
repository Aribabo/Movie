news_old <- function(keyword,start_date,end_date){
  skk <- gsub('\\+',"%2B",keyword)
  date <- as.Date(start_date):as.Date(end_date)
  date <- as.Date(date, origin="1970-01-01")
  
  library(rvest) # 웹문서분석/크롤링하는데 필요한 패키지
  news_general  <- data.frame(date=character(),title=character(), url=character())
  for (i in date){  
    dt <- format(as.Date(i,origin="1970-01-01"), "%Y.%m.%d")
    dt1 <- format(as.Date(i,origin="1970-01-01"), "%Y%m%d")
    more <- TRUE
    page <- 1 
    
    while(more){ #more(true)일 동안 반복문 시행
      print(c(dt, page)) #진행상황 확인 및 출력용으로 사용
      url1 <- paste0( 
        'https://search.naver.com/search.naver?',
        'where=news&query=', skk,
        '&sort=2',  #오래된 순으로
        '&ds=', dt,
        '&de=', dt, 
        '&docid=&nso=so%3Ada%2Cp%3Afrom', dt1, 'to', dt1,
        ',a:all&mynews=0&start=', page,  
        '&refresh_start=0'
      )

      html <- try(read_html(url1), silent=TRUE) 
      if(class(html)[1] != "try-error"){ 
        # url들 뉴스링크주소 가져오기 
        news_urls <- html %>% html_nodes(".news_area") %>% 
          html_nodes('a') %>% html_attr('href')
        news_urls2 <- news_urls[which(news_urls=='https://keep.naver.com/')+2]
        
        # 뉴스제목 가져오기 
        news_title <- html %>% html_nodes(".news_area") %>% 
          html_nodes('a') %>% html_attr('title')
        news_title2 <- news_title[!is.na(news_title)] 
        
        #데이터프레임 생성
        news1 <- as.data.frame(cbind(date= dt, title=news_title2, url=news_urls2))
        # 네이버뉴스만 가져오기
        news2 <- news1[grepl('https://n.news.naver.com/', news1$url),]
        news_general  <- rbind(news_general, news2)
        if (length(news_urls2) == 10 ){ 
          more <- TRUE
        }else{ 
          more <- FALSE 
        }
        
      }else{ 
      }
      
      if(page > 3990){
        more <- FALSE
      }else{
        page <- page + 10 #페이지 하나가 끝나면 10을 더해서 page에 저장
      }  
    }
    news_general <- news_general[!duplicated(news_general$url),]
  }
  
  return(news_general)
  rownames(news_general) <- 1:nrow(news_general)
}

news_latest <- function(keyword,start_date,end_date){
  skk <- gsub('\\+',"%2B",keyword)
  date <- as.Date(start_date):as.Date(end_date)
  date <- as.Date(date, origin="1970-01-01")
  
  library(rvest) # 웹문서분석/크롤링하는데 필요한 패키지
  news_general  <- data.frame(date=character(),title=character(), url=character())
  for (i in date){  
    dt <- format(as.Date(i,origin="1970-01-01"), "%Y.%m.%d")
    dt1 <- format(as.Date(i,origin="1970-01-01"), "%Y%m%d")
    more <- TRUE
    page <- 1 
    
    while(more){ #more(true)일 동안 반복문 시행
      print(c(dt, page)) #진행상황 확인 및 출력용으로 사용
      url1 <- paste0( 
        'https://search.naver.com/search.naver?',
        'where=news&query=', skk,
        '&sort=1',  #최신순으로
        '&ds=', dt,
        '&de=', dt, 
        '&docid=&nso=so%3Ada%2Cp%3Afrom', dt1, 'to', dt1,
        ',a:all&mynews=0&start=', page,  
        '&refresh_start=0'
      )
      
      html <- try(read_html(url1), silent=TRUE) 
      if(class(html)[1] != "try-error"){ 
        # url들 뉴스링크주소 가져오기 
        news_urls <- html %>% html_nodes(".news_area") %>% 
          html_nodes('a') %>% html_attr('href')
        news_urls2 <- news_urls[which(news_urls=='https://keep.naver.com/')+2]
        
        # 뉴스제목 가져오기 
        news_title <- html %>% html_nodes(".news_area") %>% 
          html_nodes('a') %>% html_attr('title')
        news_title2 <- news_title[!is.na(news_title)] 
        
        #데이터프레임 생성
        news1 <- as.data.frame(cbind(date= dt, title=news_title2, url=news_urls2))
        # 네이버뉴스만 가져오기
        news2 <- news1[grepl('https://n.news.naver.com/', news1$url),]
        news_general  <- rbind(news_general, news2)
        if (length(news_urls2) == 10 ){ 
          more <- TRUE
        }else{ 
          more <- FALSE 
        }
        
      }else{ 
      }
      
      if(page > 3990){
        more <- FALSE
      }else{
        page <- page + 10 #페이지 하나가 끝나면 10을 더해서 page에 저장
      }  
    }
    news_general <- news_general[!duplicated(news_general$url),]
  }
  rownames(news_general) <- 1:nrow(news_general)
  return(news_general)
}
news_topic <- function(keyword,start_date,end_date){
  skk <- gsub('\\+',"%2B",keyword)
  date <- as.Date(start_date):as.Date(end_date)
  date <- as.Date(date, origin="1970-01-01")
  
  library(rvest) # 웹문서분석/크롤링하는데 필요한 패키지
  news_general  <- data.frame(date=character(),title=character(), url=character())
  for (i in date){  
    dt <- format(as.Date(i,origin="1970-01-01"), "%Y.%m.%d")
    dt1 <- format(as.Date(i,origin="1970-01-01"), "%Y%m%d")
    more <- TRUE
    page <- 1 
    
    while(more){ #more(true)일 동안 반복문 시행
      print(c(dt, page)) #진행상황 확인 및 출력용으로 사용
      url1 <- paste0( 
        'https://search.naver.com/search.naver?',
        'where=news&query=', skk,
        '&sort=0',  #관련도순으로
        '&ds=', dt,
        '&de=', dt, 
        '&docid=&nso=so%3Ada%2Cp%3Afrom', dt1, 'to', dt1,
        ',a:all&mynews=0&start=', page,  
        '&refresh_start=0'
      )
      
      html <- try(read_html(url1), silent=TRUE) 
      if(class(html)[1] != "try-error"){ 
        # url들 뉴스링크주소 가져오기 
        news_urls <- html %>% html_nodes(".news_area") %>% 
          html_nodes('a') %>% html_attr('href')
        news_urls2 <- news_urls[which(news_urls=='https://keep.naver.com/')+2]
        
        # 뉴스제목 가져오기 
        news_title <- html %>% html_nodes(".news_area") %>% 
          html_nodes('a') %>% html_attr('title')
        news_title2 <- news_title[!is.na(news_title)] 
        
        #데이터프레임 생성
        news1 <- as.data.frame(cbind(date= dt, title=news_title2, url=news_urls2))
        # 네이버뉴스만 가져오기
        news2 <- news1[grepl('https://n.news.naver.com/', news1$url),]
        news_general  <- rbind(news_general, news2)
        if (length(news_urls2) == 10 ){ 
          more <- TRUE
        }else{ 
          more <- FALSE 
        }
        
      }else{ 
      }
      
      if(page > 3990){
        more <- FALSE
      }else{
        page <- page + 10 #페이지 하나가 끝나면 10을 더해서 page에 저장
      }  
    }
    news_general <- news_general[!duplicated(news_general$url),]
  }
  rownames(news_general) <- 1:nrow(news_general)
  return(news_general)
}




news_all <- function(keyword,start_date,end_date){
  skk <- gsub('\\+',"%2B",keyword)
  date <- as.Date(start_date):as.Date(end_date)
  date <- as.Date(date, origin="1970-01-01")
  
  library(rvest) # 웹문서분석/크롤링하는데 필요한 패키지
  news_general  <- data.frame(date=character(),title=character(), url=character())
  for (i in date){
    dt <- format(as.Date(i,origin="1970-01-01"), "%Y.%m.%d")
    dt1 <- format(as.Date(i,origin="1970-01-01"), "%Y%m%d")
    print(dt)
    for(j in 1:3){
      more <- TRUE
      page <- 1 
      
      while(more){ #more(true)일 동안 반복문 시행
        
        url1 <- paste0( 
          'https://search.naver.com/search.naver?',
          'where=news&query=', skk,
          '&sort=',j,  #오래된 순으로
          '&ds=', dt,
          '&de=', dt, 
          '&docid=&nso=so%3Ada%2Cp%3Afrom', dt1, 'to', dt1,
          ',a:all&mynews=0&start=', page,  
          '&refresh_start=0'
        )
        
        html <- try(read_html(url1), silent=TRUE) 
        if(class(html)[1] != "try-error"){ 
          # url들 뉴스링크주소 가져오기 
          news_urls <- html %>% html_nodes(".news_area") %>% 
            html_nodes('a') %>% html_attr('href')
          news_urls2 <- news_urls[which(news_urls=='https://keep.naver.com/')+2]
          
          # 뉴스제목 가져오기 
          news_title <- html %>% html_nodes(".news_area") %>% 
            html_nodes('a') %>% html_attr('title')
          news_title2 <- news_title[!is.na(news_title)] 
          
          #데이터프레임 생성
          news1 <- as.data.frame(cbind(date= dt, title=news_title2, url=news_urls2))
          # 네이버뉴스만 가져오기
          news2 <- news1[grepl('https://n.news.naver.com/', news1$url),]
          news_general  <- rbind(news_general, news2)
          if (length(news_urls2) == 10 ){ 
            more <- TRUE
          }else{ 
            more <- FALSE 
          }
          
        }else{ 
        }
        
        if(page > 3990){
          more <- FALSE
        }else{
          page <- page + 10 #페이지 하나가 끝나면 10을 더해서 page에 저장
        }  
      }
      if(page < 3990){
        break
      }else{
        
      }
      news_general <- news_general[!duplicated(news_general$url),]
    }
    
  }
  
  return(news_general)
  rownames(news_general) <- 1:nrow(news_general)
}
