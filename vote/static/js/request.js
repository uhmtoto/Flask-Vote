$(document).ready(function () {
    $('.vote').click(function () {
        c_name = $(this).attr('data-name')
        c_part = $(this).attr('data-part')
        swal.mixin({
            input: 'text',
            inputAttributes: {
                autocapitalize: 'off'
            },
            showLoaderOnConfirm: true,
            confirmButtonText: '확인 &rarr;',
            showCancelButton: true,
            preConfirm: (u_key) => {
                return fetch('/vote', {
                    method: "POST",
                    body: JSON.stringify({
                        'value': c_name,
                        'part': c_part,
                        'key': u_key
                    }),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error(response.statusText)
                        }
                    })
                    .catch(error => {
                        swal.showValidationMessage(
                            '잘못된 코드이거나 이미 해당 코드로 투표 되었습니다.'
                        )
                    })
            },
            allowOutsideClick: () => !swal.isLoading()
        }).queue([
            {
                title: '정말로 ' + c_part + '에 ' + c_name + ' 후보를 선택 하시겠습니까?',
                text: '맞다면 본인 확인 코드를 입력해주세요.'
            }
        ]).then((result) => {
            if (result.value) {
                swal({
                    title: '투표가 정상적으로 처리되었습니다!',
                    confirmButtonText: '창닫기'
                })
            }
        })
    });
});